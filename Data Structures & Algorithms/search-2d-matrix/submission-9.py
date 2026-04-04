class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        '''matrix -> [ [1, 2],
                       [3, 4],
                       [7, 9], ]

            my solution is in m * log n  

            the actual solution is to find the row and THEN find the element

            we do not have to check every row, we can be sure that the other 
                half is not needed anymore
                i.e [1,2] [3,4] [5, 6] so if target < 3, we look one row below
            '''
        m = len(matrix) #number of sub-lists inside matrix
        n = len(matrix[0]) #length of each sub-list

        top = 0
        bottom = m-1

        while top <= bottom:
            mid = top+ (bottom-top)//2
            if target < matrix[mid][0]:
                bottom = mid - 1
            elif target > matrix[mid][n-1]:
                top = mid+1
            else:
                low = 0
                high = n - 1
                while low <= high:
                    mid2 = low+ (high-low) // 2
                    if matrix[mid][mid2] == target:
                        return True
                    elif matrix[mid][mid2] < target:
                        low = mid2 + 1
                    else:
                        high = mid2 - 1
                return False
        return False

