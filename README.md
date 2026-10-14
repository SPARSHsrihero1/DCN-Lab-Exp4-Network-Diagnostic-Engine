# Network Diagnostic and Topology Path Analyzer Engine (DCN Lab - Experiment 4)

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Linux%20%7C%20macOS-lightgrey.svg)]()

A comprehensive, cross-platform network diagnostic and telemetry pipeline developed in Python. This project fulfills all requirements for **Experiment 4: Network Diagnostic and Topology Path Analyzer Engine** for the **Data Communication and Networks (DCN)** laboratory curriculum.

---

## 👥 Batch & Team Details
- **Batch ID:** `DCN_17_02`
- **Group:** `4`
- **Department:** Computer Science and Engineering

| # | Student Name | SAP ID | Role / Module Assigned |
|---|---|---|---|
| **1** | **Sparsh Srivastava** | `590022251` | **Project Lead** • Core Engine Architecture & Protocol Theory |
| **2** | **Aayushman Kothari** | `590025499` | Subprocess Execution Wrapper & DNS Resolution Engine |
| **3** | **Yasharth Jaiswal** | `590023687` | Regular Expression Parsing & Metric Extraction Core |
| **4** | **Satvik Arora** | `590028424` | Latency Benchmarking & Hop-by-Hop Topology Path Analytics |
| **5** | **Yashvardhan Singh** | `590021777` | Temporal Latency Heatmaps & Live Telemetry Demonstration |

---

## 🎯 Lab Objectives & Students Tasks

1. **Subprocess Diagnostic Wrapper (Task 1):**
   - Cleanly execute low-level operating system commands (`ping`, `tracert`/`traceroute`, and `nslookup`) using Python's `subprocess` without shell injection risks (`shell=False`).
   - Cross-platform support automatically adapting flags for Windows (`-n`, `-d`) and Linux/macOS (`-c`, `-n`).
2. **Stdout Parsing & Metric Extraction (Task 2):**
   - Parse unstructured terminal outputs using dual regex patterns.
   - Extract numerical metrics: Minimum RTT, Average RTT, Maximum RTT, Packet Loss %, and ordered intermediate router hops with hop latency.
3. **Statistical Charts & Latency Heatmaps (Task 3):**
   - High-resolution comparative bar plots across network tiers (Local Gateway, Cloudflare, Google, GitHub).
   - Hop-by-hop latency progression curves exposing ISP transit bottlenecks.
   - Diurnal latency heatmaps analyzing peak-hour network congestion and jitter.

---

## 🎓 Academic Syllabus Grounding

- **Unit I (Basic Computer Networking & Topologies):** OSI/TCP-IP layer boundaries, packet encapsulation, and traversal across LAN, MAN, and WAN.
- **Unit IV (Network Layer & IP Datagram):** IPv4/IPv6 addressing, subnet masking, loopback testing (`127.0.0.1`), and the **8-bit Time-To-Live (TTL)** field triggering **ICMP Type 11 (Time Exceeded)** messages to discover intermediate router hops.
- **Unit V (Transport Layer & Network Performance):** Transport socket addressing, delay jitter, bufferbloat, and diurnal Quality of Service (QoS) variations.

---

## 📊 Visual Analytics Preview

| Multi-Target Latency Comparison | Hop-by-Hop Path Anatomy |
|:---:|:---:|
| ![Latency Chart](figures/latency_chart.png) | ![Hop Curve](figures/hop_curve.png) |

| Diurnal Congestion Heatmap |
|:---:|
| ![Latency Heatmap](figures/latency_heatmap.png) |

---

## 🚀 Getting Started

### 1. Prerequisites
Ensure you have Python 3.8+ installed:
```bash
python --version
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the Network Diagnostic Engine
```bash
python network_analyzer.py
```

### 4. Regenerate Analytics Plots
```bash
python generate_charts.py
```

### 5. Build or Update the PowerPoint Presentation
```bash
python make_presentation.py
```
This generates `Network_Diagnostic_Analyzer_Exp4_Syllabus_Team.pptx` complete with all 12 slides, speaker notes, and embedded charts.

---

## 📁 Project Structure

```
DCN-Lab-Exp4-Network-Diagnostic-Engine/
│
├── network_analyzer.py       # Core cross-platform diagnostic & regex parsing engine
├── generate_charts.py        # Matplotlib visualization script for bar charts, curves & heatmaps
├── make_presentation.py      # Automated PPTX presentation generator with team allocations
├── requirements.txt          # Python dependencies
├── README.md                 # Project documentation and guide
│
├── figures/                  # Generated high-resolution diagnostic plots
│   ├── latency_chart.png     # Multi-target RTT bar chart
│   ├── hop_curve.png         # Hop-by-hop latency curve
│   └── latency_heatmap.png   # Time-of-day jitter & congestion heatmap
│
└── Network_Diagnostic_Analyzer_Exp4_Syllabus_Team.pptx # 12-slide lab presentation
```

---

## 📜 License
This project is open-source and available under the [MIT License](LICENSE).
