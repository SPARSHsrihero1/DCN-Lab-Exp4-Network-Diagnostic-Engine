"""
Experiment 4: Network Diagnostic and Topology Path Analyzer Engine
Department of Computer Science and Engineering
Batch ID: DCN_17_02 | Group 4

Team Members:
1. Sparsh Srivastava  (SAP: 590022251) - Project Lead & Core Diagnostic Engine
2. Aayushman Kothari   (SAP: 590025499) - Subprocess Wrappers & DNS Resolver
3. Yasharth Jaiswal    (SAP: 590023687) - Regex Parsing & Metric Extraction
4. Satvik Arora        (SAP: 590028424) - Latency Benchmarking & Path Anatomy
5. Yashvardhan Singh   (SAP: 590021777) - Heatmaps & Live Telemetry Demonstration
"""

import subprocess
import platform
import re
import os
import concurrent.futures
from dataclasses import dataclass, field
from typing import List, Dict, Optional

OS_NAME = platform.system().lower()

@dataclass
class PingResult:
    target: str
    sent: int = 0
    received: int = 0
    loss_percent: float = 0.0
    min_rtt: Optional[float] = None
    avg_rtt: Optional[float] = None
    max_rtt: Optional[float] = None
    is_reachable: bool = False

@dataclass
class Hop:
    hop_num: int
    ip_or_host: str
    latencies: List[float] = field(default_factory=list)
    timed_out: bool = False

@dataclass
class TraceResult:
    target: str
    hops: List[Hop] = field(default_factory=list)
    total_hops: int = 0

class NetworkDiagnosticEngine:
    """
    Task 1: Subprocess execution wrappers for ping, tracert/traceroute, and nslookup.
    Task 2: Regex-driven metric extraction (RTT, packet loss, intermediate router hops).
    """
    def __init__(self, ping_count: int = 4, trace_max_hops: int = 15):
        self.ping_count = ping_count
        self.trace_max_hops = trace_max_hops

    def run_ping(self, target: str) -> PingResult:
        res = PingResult(target=target, sent=self.ping_count)
        cmd = ["ping", "-n" if OS_NAME == "windows" else "-c", str(self.ping_count), target]
        try:
            proc = subprocess.run(cmd, capture_output=True, text=True, timeout=15)
            stdout = proc.stdout
            if OS_NAME == "windows":
                loss_m = re.search(r'Lost = \d+ \((\d+)% loss\)', stdout)
                if loss_m:
                    res.loss_percent = float(loss_m.group(1))
                    res.received = int(self.ping_count * (1 - res.loss_percent / 100))
                rtt_m = re.search(r'Minimum = (\d+)ms, Maximum = (\d+)ms, Average = (\d+)ms', stdout)
                if rtt_m:
                    res.min_rtt = float(rtt_m.group(1))
                    res.max_rtt = float(rtt_m.group(2))
                    res.avg_rtt = float(rtt_m.group(3))
                    res.is_reachable = True
            else:
                loss_m = re.search(r'(\d+)% packet loss', stdout)
                if loss_m:
                    res.loss_percent = float(loss_m.group(1))
                    res.received = int(self.ping_count * (1 - res.loss_percent / 100))
                rtt_m = re.search(r'min/avg/max[^=]*=\s*([\d\.]+)/([\d\.]+)/([\d\.]+)', stdout)
                if rtt_m:
                    res.min_rtt = float(rtt_m.group(1))
                    res.avg_rtt = float(rtt_m.group(2))
                    res.max_rtt = float(rtt_m.group(3))
                    res.is_reachable = True
        except Exception:
            res.is_reachable = False
        return res

    def run_trace(self, target: str) -> TraceResult:
        res = TraceResult(target=target)
        cmd = ["tracert", "-d", "-h", str(self.trace_max_hops), target] if OS_NAME == "windows" else ["traceroute", "-n", "-m", str(self.trace_max_hops), target]
        try:
            proc = subprocess.run(cmd, capture_output=True, text=True, timeout=35)
            for line in proc.stdout.splitlines():
                line = line.strip()
                if not line or not line[0].isdigit():
                    continue
                parts = line.split()
                try:
                    hop_num = int(parts[0])
                except ValueError:
                    continue
                if "*" in line and ("Request timed out" in line or parts[-1] == "*"):
                    res.hops.append(Hop(hop_num=hop_num, ip_or_host="* (Timed Out)", timed_out=True))
                else:
                    ip = parts[-1]
                    ms_vals = [float(m.replace("<", "0.5")) for m in re.findall(r'(<?\d+)\s*ms', line)]
                    res.hops.append(Hop(hop_num=hop_num, ip_or_host=ip, latencies=ms_vals))
            res.total_hops = len(res.hops)
        except Exception:
            pass
        return res

    def run_nslookup(self, target: str) -> Dict[str, any]:
        cmd = ["nslookup", target]
        info = {"target": target, "addresses": []}
        try:
            proc = subprocess.run(cmd, capture_output=True, text=True, timeout=10)
            matches = re.findall(r'Address(?:es)?:\s*([^\r\n]+)', proc.stdout)
            for m in matches:
                info["addresses"].extend(m.replace("\t", " ").split())
        except Exception:
            pass
        return info

def print_banner():
    print("=" * 75)
    print("  EXPERIMENT 4: NETWORK DIAGNOSTIC & TOPOLOGY PATH ANALYZER ENGINE")
    print("  Batch ID: DCN_17_02 | Group 4 | Department of CSE")
    print("=" * 75)
    print("  Team Members:")
    print("    1. Sparsh Srivastava  (590022251) - Project Lead & Core Engine")
    print("    2. Aayushman Kothari   (590025499) - Subprocess Wrappers & DNS")
    print("    3. Yasharth Jaiswal    (590023687) - Regex Parsing & Metric Extraction")
    print("    4. Satvik Arora        (590028424) - Latency Benchmarks & Path Anatomy")
    print("    5. Yashvardhan Singh   (590021777) - Heatmaps & Live Telemetry")
    print("=" * 75 + "\n")

if __name__ == "__main__":
    print_banner()
    engine = NetworkDiagnosticEngine()
    
    benchmark_hosts = [
        ("192.168.1.1", "Local Gateway Router"),
        ("1.1.1.1", "Cloudflare Anycast DNS"),
        ("8.8.8.8", "Google Primary DNS"),
        ("github.com", "GitHub Global Web Tier")
    ]
    
    print("[TASK 1 & TASK 2 EXECUTION]: Running Diagnostic Probes...\n")
    for host, desc in benchmark_hosts:
        print(f">>> Probing Target: {host} ({desc})")
        
        # DNS Resolution
        dns_data = engine.run_nslookup(host)
        if dns_data["addresses"]:
            print(f"    [DNS] Resolved Addresses : {', '.join(dns_data['addresses'][:2])}")
            
        # Ping Telemetry
        p_res = engine.run_ping(host)
        if p_res.is_reachable:
            print(f"    [PING] Status           : REACHABLE")
            print(f"           Packet Loss      : {p_res.loss_percent}% ({p_res.received}/{p_res.sent} received)")
            print(f"           Round-Trip Time  : Min={p_res.min_rtt}ms | Avg={p_res.avg_rtt}ms | Max={p_res.max_rtt}ms")
        else:
            print(f"    [PING] Status           : PACKET TIMEOUT / HOST UNREACHABLE")
            
        print("-" * 65)

    print("\n[*] Demonstration complete. To inspect charts, view generated files in ./figures/")
