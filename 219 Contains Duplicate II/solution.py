

def containsNearbyDuplicate(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: bool
    """

    dict_num_to_index = {}
    for idx, num in enumerate(nums):
        if num not in dict_num_to_index:
            dict_num_to_index[num] = idx
        else:
            prev_idx = dict_num_to_index[num]
            if idx - prev_idx <= k:
                return True
            dict_num_to_index[num] = idx

    return False

if __name__ == '__main__':
    nums = [1, 0, 1, 1, 2, 3]
    k = 2
    print containsNearbyDuplicate(nums, k)