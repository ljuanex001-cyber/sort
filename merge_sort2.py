def merge_sort(arr):
    """
    归并排序算法
    时间复杂度: O(n log n)
    空间复杂度: O(n)
    """
    # 如果数组长度小于等于1，直接返回（已经是排序好的）
    if len(arr) <= 1:
        return arr
    
    # 使用统一的分区逻辑将数组拆分为两半
    left_part, right_part = partition_data(arr, num_partitions=2)
    
    # 递归对左右分区进行排序
    left = merge_sort(left_part)
    right = merge_sort(right_part)
    
    # 合并两个有序数组
    return merge(left, right)


def partition_data(arr, num_partitions=2):
    """
    将数组拆分为 num_partitions 份，尽量保持每份大小接近。
    例如: [1, 2, 3, 4, 5] -> [[1, 2, 3], [4, 5]] (num_partitions=2)
    """
    if not isinstance(num_partitions, int) or num_partitions <= 0:
        raise ValueError("num_partitions 必须是正整数")

    total = len(arr)
    base_size, remainder = divmod(total, num_partitions)

    partitions = []
    start = 0
    for idx in range(num_partitions):
        current_size = base_size + (1 if idx < remainder else 0)
        end = start + current_size
        partitions.append(arr[start:end])
        start = end

    return partitions

def merge(left, right):
    """
    合并两个有序数组
    """
    result = []
    i = j = 0
    
    # 比较两个数组的元素，将较小的放入结果数组
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    # 将剩余的元素添加到结果数组
    result.extend(left[i:])
    result.extend(right[j:])
    
    return result


# 测试代码
if __name__ == "__main__":
    # 测试用例
    test_arrays = [
        [64, 34, 25, 12, 22, 11, 90],
        [3, -1, 0, 5, -2],
        [1],
        [],
        [5, 5, 5, 1],
        [1, 2, 3, 4, 5],  # 已排序
        [5, 4, 3, 2, 1],  # 逆序
    ]
    
    print("归并排序测试:")
    print("-" * 40)
    
    for arr in test_arrays:
        original = arr.copy()
        sorted_arr = merge_sort(arr)
        print(f"原始数组: {original}")
        print(f"排序结果: {sorted_arr}")
        print("-" * 40)

    partition_test_cases = [
        ([1, 2, 3, 4, 5], 2, [[1, 2, 3], [4, 5]]),
        ([1, 2, 3, 4, 5, 6, 7], 3, [[1, 2, 3], [4, 5], [6, 7]]),
        ([], 2, [[], []]),
    ]

    print("分区逻辑测试:")
    print("-" * 40)

    for data, parts, expected in partition_test_cases:
        result = partition_data(data, parts)
        print(f"原始数据: {data}, 分区数: {parts}")
        print(f"分区结果: {result}")
        if result != expected:
            raise AssertionError(f"分区结果不符合预期: {result} != {expected}")
        print("-" * 40)
