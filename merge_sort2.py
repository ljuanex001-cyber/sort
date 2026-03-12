def merge_sort(arr):
    """
    归并排序算法
    时间复杂度: O(n log n)
    空间复杂度: O(n)
    """
    # 如果数组长度小于等于1，直接返回（已经是排序好的）
    if len(arr) <= 1:
        return arr
    
    # 找到中间位置，将数组分成两半
    left_part, right_part = split_array(arr)

    # 递归对左右部分进行排序
    left = merge_sort(left_part)
    right = merge_sort(right_part)
    
    # 合并两个有序数组
    return merge(left, right)


def split_array(arr):
    """
    将数组按中点拆分成左右两部分
    """
    mid = len(arr) // 2
    return arr[:mid], arr[mid:]

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
