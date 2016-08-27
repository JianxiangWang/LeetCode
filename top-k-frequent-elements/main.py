#encoding: utf-8
import heapq

# Given [1,1,1,2,2,3] and k = 2, return [1,2].
def topKFrequent(nums, k):

    dict_num_to_freq = {}
    # do count, O(n)
    for num in nums:
        if num not in dict_num_to_freq:
            dict_num_to_freq[num] = 0
        dict_num_to_freq[num] += 1
    # find top K in dict_num_to_freq, O(nlogK)
    heap = []

    for num in dict_num_to_freq:
        freq = dict_num_to_freq[num]

        if len(heap) < k:
            heapq.heappush(heap, (freq, num))
        else:
            # 比最小的要大, 干掉!
            if freq > heap[0][0]:
                heapq.heapreplace(heap, (freq, num))

    # output
    return [num for _, num in heap]


if __name__ == '__main__':
    nums = [1,1,1,2,2,3,3,3,3]
    k = 2

    print (topKFrequent(nums, k))
