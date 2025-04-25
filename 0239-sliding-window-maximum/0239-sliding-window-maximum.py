import heapq

class Solution(object):
    def maxSlidingWindow(self, nums, k):
        ans = []
        max_heap = []

        for i in range(k):
            heapq.heappush(max_heap, (-nums[i], i))
        ans.append(-max_heap[0][0])  
        for i in range(k, len(nums)):
            heapq.heappush(max_heap, (-nums[i], i))
            while max_heap[0][1] <= i - k:
                heapq.heappop(max_heap)
            ans.append(-max_heap[0][0])  

        return ans
