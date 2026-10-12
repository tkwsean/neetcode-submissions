class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        target_row = -1
        top, bottom = 0, len(matrix)-1
        while top <= bottom:
            mid = top + (bottom - top) // 2
            if target > matrix[mid][-1]:
                top = mid+1
            elif target < matrix[mid][0]:
                bottom = mid-1
            else:
                target_row = mid
                break
        if target_row == -1:
            return False
        left, right = 0, len(matrix[0])-1
        while left <= right:
            mid = left + (right - left) // 2
            if target > matrix[target_row][mid]:
                left = mid+1
            elif target < matrix[target_row][mid]:
                right = mid - 1
            else:
                return True
        return False
                