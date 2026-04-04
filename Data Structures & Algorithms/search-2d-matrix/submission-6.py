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

        index = 0

        while index < m:
            if (target >= matrix[index][0] and target <= matrix[index][n-1]):
                low = 0
                high = n - 1
                while low <= high:
                    mid = low+ (high-low) // 2
                    if matrix[index][mid] == target:
                        return True
                    elif matrix[index][mid] < target:
                        low = mid + 1
                    else:
                        high = mid - 1
                return False
            else:
                index+=1
        return False

