
def intersection(nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: List[int]
    """

    s1 = set(nums1)
    s2 = set(nums2)

    return list(s1 & s2)


if __name__ == '__main__':

    nums1 = [1, 2, 2, 1]
    nums2 = [2, 2]

    print intersection(nums1, nums2)


