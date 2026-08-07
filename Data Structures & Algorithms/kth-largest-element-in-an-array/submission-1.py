class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        #[2,3,1,1,5,5,4], k = 3
        #[1,1,2,3,4,5,5]
        heapq.heapify(nums)

        numPop = len(nums) - k
        for i in range(numPop):
            heapq.heappop(nums)

        return nums[0]