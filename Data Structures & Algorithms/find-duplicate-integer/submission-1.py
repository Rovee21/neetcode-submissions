class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        #input: [1,2,3,2,2] -> look through the array and find repeat val -> output:repeat val
        #optimal solution: use fast and slow pointers to find the intersection point and 
        #after that, find intersection with point starting at 0 and point at intersection
        #input: [1,2,3,2,2], slow = 2, fast = 2, slow2 = 2

        slow, fast = 0,0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow==fast:
                break 
        
        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow2==slow:
                return slow


        

        