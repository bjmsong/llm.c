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

# 找出每个version下time最小且bandwidth最大的结果
optimal_results = {}
for version in df['Version'].unique():
    # 筛选特定version的数据
    version_data = df[df['Version'] == version]
    # 找出time最小的记录
    min_time_row = version_data.loc[version_data['time (ms)'].idxmin()]
    # 找出bandwidth最大的记录
    max_bandwidth_row = version_data.loc[version_data['bandwidth (GB/s)'].idxmax()]
    # 判断是否为同一行数据
    if min_time_row.name == max_bandwidth_row.name:
        optimal_results[version] = {
            'block size': min_time_row['block size'],
            'time (ms)': min_time_row['time (ms)'],
            'bandwidth (GB/s)': max_bandwidth_row['bandwidth (GB/s)']
        }

# 输出结果
print("不同version下time最小，bandwidth最大的结果:")
for version, result in optimal_results.items():
    print(f"Version {version}: Block Size {result['block size']}, Time {result['time (ms)']} ms, Bandwidth {result['bandwidth (GB/s)']} GB/s")

# 找出整体最优的version
overall_best_time = df.loc[df['time (ms)'].idxmin()]
overall_best_bandwidth = df.loc[df['bandwidth (GB/s)'].idxmax()]
print("\n整体最优的version:")
print(f"Time: Version {overall_best_time['Version']} at Block Size {overall_best_time['block size']} with {overall_best_time['time (ms)']} ms")
print(f"Bandwidth: Version {overall_best_bandwidth['Version']} at Block Size {overall_best_bandwidth['block size']} with {overall_best_bandwidth['bandwidth (GB/s)']} GB/s")