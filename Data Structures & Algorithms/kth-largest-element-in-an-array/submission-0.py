class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        #[2,3,1,1,5,5,4], k = 3
        #[1,1,2,3,4,5,5]


        #sort and find -k
        nums.sort()
        return nums[-k]