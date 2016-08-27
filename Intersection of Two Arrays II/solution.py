
def intersect(nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """

        dict_num1_to_count = {}
        dict_num2_to_count = {}

        for x in nums1:
            if x not in dict_num1_to_count:
                dict_num1_to_count[x] = 0
            dict_num1_to_count[x] += 1

        for x in nums2:
            if x not in dict_num2_to_count:
                dict_num2_to_count[x] = 0
            dict_num2_to_count[x] += 1

        t = []
        for common_num in dict_num1_to_count:
            if common_num in dict_num2_to_count:
                t.extend([common_num] * min(dict_num1_to_count[common_num], dict_num2_to_count[common_num]))

        return t


if __name__ == '__main__':
    nums1 = [1, 1]
    nums2 = [1]
    print intersect(nums1, nums2)