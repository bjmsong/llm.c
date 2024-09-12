import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# 数据
data = {
    'block size': ['32', '32', '32', '32', '32', '32',
                   '64', '64', '64', '64', '64', '64',
                   '128', '128', '128', '128', '128', '128',
                   '256', '256', '256', '256', '256', '256',
                   '512', '512', '512', '512', '512', '512',
                   '1024', '1024', '1024', '1024', '1024', '1024'],
    'Version': ['v1', 'v2', 'v3', 'v4', 'v5', 'v6'] * 6,
    'time (ms)': [1.3385, 0.8807, 0.4706, 0.4101, 0.5348, 0.4294,
                  1.3094, 0.8541, 0.4735, 0.4448, 0.4096, 0.4147,
                  1.4282, 0.8056, 0.5252, 0.4734, 0.4022, 0.3976,
                  1.4427, 0.8613, 0.4699, 0.4601, 0.3894, 0.4129,
                  1.8802, 0.9059, 0.4795, 0.4567, 0.4505, 0.4596,
                  3.6318, 1.5001, 0.4759, 0.4602, 0.5951, 0.617],
    'bandwidth (GB/s)': [37.6, 57.15, 106.95, 122.73, 94.11, 117.2,
                         38.44, 58.93, 106.3, 113.15, 122.89, 121.37,
                         35.24, 62.48, 95.83, 106.32, 125.13, 126.6,
                         34.89, 58.44, 107.11, 109.38, 129.25, 121.9,
                         26.77, 55.56, 104.97, 110.22, 111.73, 109.52,
                         13.86, 33.55, 105.76, 109.38, 84.57, 81.57]
}

# 创建DataFrame
df = pd.DataFrame(data)

# 计算每个block size下最优的version
optimal_versions_time = df.loc[df.groupby('block size')['time (ms)'].idxmin()]
optimal_versions_bandwidth = df.loc[df.groupby('block size')['bandwidth (GB/s)'].idxmax()]

# 绘制柱状图
fig, ax = plt.subplots(2, 1, figsize=(12, 10))

# 绘制时间图
bar_width = 0.15
indices = np.arange(len(df['block size'].unique()))
for i, version in enumerate(df['Version'].unique()):
    times = df[df['Version'] == version]['time (ms)']
    ax[0].bar(indices + i * bar_width, times, bar_width, label=version)

# 标出每个block size下time最小的version
for idx, block_size in enumerate(df['block size'].unique()):
    version = optimal_versions_time[optimal_versions_time['block size'] == block_size]['Version'].values[0]
    min_time = df[(df['block size'] == block_size) & (df['Version'] == version)]['time (ms)'].values[0]
    ax[0].text(idx, min_time, f'{version}', ha='center', va='bottom')

ax[0].set_title('Time (ms) by Block Size and Version')
ax[0].set_ylabel('Time (ms)')
ax[0].set_xticks(indices + bar_width * 2)
ax[0].set_xticklabels(df['block size'].unique())
ax[0].legend()

# 绘制带宽图
for i, version in enumerate(df['Version'].unique()):
    bandwidths = df[df['Version'] == version]['bandwidth (GB/s)']
    ax[1].bar(indices + i * bar_width, bandwidths, bar_width, label=version)

# 标出每个block size下bandwidth最大的version
for idx, block_size in enumerate(df['block size'].unique()):
    version = optimal_versions_bandwidth[optimal_versions_bandwidth['block size'] == block_size]['Version'].values[0]
    max_bandwidth = df[(df['block size'] == block_size) & (df['Version'] == version)]['bandwidth (GB/s)'].values[0]
    ax[1].text(idx, max_bandwidth, f'{version}', ha='center', va='bottom')

ax[1].set_title('Bandwidth (GB/s) by Block Size and Version')
ax[1].set_ylabel('Bandwidth (GB/s)')
ax[1].set_xticks(indices + bar_width * 2)
ax[1].set_xticklabels(df['block size'].unique())
ax[1].legend()

plt.tight_layout()
plt.savefig('time_and_bandwidth_comparison.png')
plt.show()

# 输出每个block size下最优的version
print("每个block size下最优的version（time最小，bandwidth最大）:")
for block_size in df['block size'].unique():
    print(f"{block_size}: Time - {optimal_versions_time[optimal_versions_time['block size'] == block_size]['Version'].values[0]}, "
          f"Bandwidth - {optimal_versions_bandwidth[optimal_versions_bandwidth['block size'] == block_size]['Version'].values[0]}")

# 找出最优的block size和version
overall_best_time = df.loc[df['time (ms)'].idxmin()]
overall_best_bandwidth = df.loc[df['bandwidth (GB/s)'].idxmax()]
print("\n最优的block size和version（time最小，bandwidth最大）:")
print(f"Time: {overall_best_time['Version']} at {overall_best_time['block size']}, "
      f"Bandwidth: {overall_best_bandwidth['Version']} at {overall_best_bandwidth['block size']}")