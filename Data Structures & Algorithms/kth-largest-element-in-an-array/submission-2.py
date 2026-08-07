class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        #keep taking the max until k
        # if k==1:
        #     return max(nums)
        # for i in range(k-1):
        #     nums.remove(max(nums))
        
        # return max(nums)

        #[1,2,3,4,5]

        heapq.heapify(nums)
        
        for i in range(len(nums)-k):
            heapq.heappop(nums)

        return heapq.heappop(nums)
