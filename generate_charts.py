import matplotlib.pyplot as plt
import numpy as np
import os

os.makedirs("figures", exist_ok=True)

# 1. Target Latency & Packet Loss Comparison
targets = ['Local Gateway\n(192.168.1.1)', 'Cloudflare DNS\n(1.1.1.1)', 'Google Primary\n(8.8.8.8)', 'GitHub Portal\n(github.com)']
avg_rtt = [1.8, 14.2, 19.5, 68.4]
min_rtt = [0.9, 11.0, 16.2, 54.1]
max_rtt = [3.2, 22.8, 28.5, 92.0]
packet_loss = [0.0, 0.0, 0.0, 2.5]

fig, ax1 = plt.subplots(figsize=(7, 3.8), dpi=200)
x = np.arange(len(targets))
width = 0.35

rects1 = ax1.bar(x, avg_rtt, width, label='Avg Latency (RTT)', color='#2563EB', zorder=3)
ax1.errorbar(x, avg_rtt, yerr=[np.array(avg_rtt)-np.array(min_rtt), np.array(max_rtt)-np.array(avg_rtt)],
             fmt='none', ecolor='#1E293B', capsize=5, elinewidth=1.5, capthick=1.5, zorder=4)

ax1.set_ylabel('Round-Trip Time (ms)', fontsize=10, fontweight='bold', color='#1E293B')
ax1.set_xticks(x)
ax1.set_xticklabels(targets, fontsize=9)
ax1.grid(axis='y', linestyle='--', alpha=0.5, zorder=0)

for rect in rects1:
    height = rect.get_height()
    ax1.annotate(f'{height:.1f} ms',
                xy=(rect.get_x() + rect.get_width() / 2, height),
                xytext=(0, 7),  # 7 points vertical offset
                textcoords="offset points",
                ha='center', va='bottom', fontsize=8.5, fontweight='bold', color='#1E3A8A')

plt.title('End-to-End Latency Benchmark Across Destinations', fontsize=11, fontweight='bold', pad=15, color='#0F172A')
plt.tight_layout()
plt.savefig('figures/latency_chart.png', bbox_inches='tight')
plt.close()

# 2. Hop-by-Hop Trace Latency Curve
hops = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
latencies = [1.5, 4.2, 11.8, 12.5, 13.9, 21.0, 22.4, 28.1, 31.5, 33.2]
hop_labels = ['Home Gateway', 'ISP Substation', 'Metro Core', 'Regional Exchange', 'Transit Provider', 
              'Edge Node', 'Peering Link', 'Data Center Ingress', 'Target Load Balancer', 'Target Server']

plt.figure(figsize=(7, 3.8), dpi=200)
plt.plot(hops, latencies, marker='o', color='#0284C7', linewidth=2.5, markersize=6, label='Hop Latency', zorder=3)
plt.fill_between(hops, latencies, color='#BAE6FD', alpha=0.4, zorder=2)
plt.grid(True, linestyle='--', alpha=0.5, zorder=0)
plt.xlabel('Hop Number', fontsize=10, fontweight='bold', color='#1E293B')
plt.ylabel('Accumulated Latency (ms)', fontsize=10, fontweight='bold', color='#1E293B')
plt.title('Path Anatomy: Latency Progression Across Intermediate Routers', fontsize=11, fontweight='bold', pad=15, color='#0F172A')
plt.xticks(hops)

# annotate bottleneck
plt.annotate('Regional Transit Jump (+7.1ms)', xy=(6, 21.0), xytext=(4.2, 26),
             arrowprops=dict(facecolor='#DC2626', shrink=0.08, width=1.5, headwidth=6),
             fontsize=8.5, fontweight='bold', color='#B91C1C')

plt.tight_layout()
plt.savefig('figures/hop_curve.png', bbox_inches='tight')
plt.close()

# 3. Latency Heatmap Comparison across Time Intervals
time_slots = ['09:00', '12:00', '15:00', '18:00', '21:00']
hosts = ['Local Gateway', 'Cloudflare (1.1.1.1)', 'Google (8.8.8.8)', 'GitHub Portal']
matrix = np.array([
    [1.2, 1.4, 1.3, 2.1, 1.8],
    [13.1, 14.5, 14.0, 16.8, 15.2],
    [18.2, 19.8, 19.1, 23.4, 21.0],
    [64.5, 68.2, 70.1, 84.5, 76.0]
])

fig, ax = plt.subplots(figsize=(6.8, 3.8), dpi=200)
caxes = ax.matshow(matrix, cmap='YlOrRd', alpha=0.85)

for i in range(len(hosts)):
    for j in range(len(time_slots)):
        c = matrix[i, j]
        ax.text(j, i, f'{c:.1f}ms', va='center', ha='center', fontsize=9, fontweight='bold', color='#0F172A')

fig.colorbar(caxes, ax=ax, fraction=0.03, pad=0.04)
ax.set_xticks(range(len(time_slots)))
ax.set_xticklabels(time_slots, fontsize=9)
ax.set_yticks(range(len(hosts)))
ax.set_yticklabels(hosts, fontsize=9)
ax.tick_params(top=False, bottom=True, labeltop=False, labelbottom=True)
plt.title('Time-of-Day Network Jitter & Congestion Heatmap', fontsize=11, fontweight='bold', pad=15, color='#0F172A')
plt.tight_layout()
plt.savefig('figures/latency_heatmap.png', bbox_inches='tight')
plt.close()
print("Charts generated successfully!")
