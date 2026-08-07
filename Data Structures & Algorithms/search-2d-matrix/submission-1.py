class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #binary search to find the row
        ROWS,COLS = len(matrix),len(matrix[0])
        t = 0
        b = len(matrix)-1

        while(t<=b):
            m = (t+b)//2
            if(matrix[m][-1]<target):
                t = m +1
            elif(matrix[m][0] > target):
                b = m -1
            else:
                break
        if not (t<=b):
            return False
        #binary search to find the number  
        l = 0
        r = COLS-1
        while(l<=r):
            middle = (l+r)//2

            if(matrix[m][middle]<target):
                l = middle +1
            elif(matrix[m][middle]>target):
                r = middle -1
            else:
                return True

        return False