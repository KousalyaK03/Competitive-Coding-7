# Explain your approach briefly:
# The matrix is row-wise and column-wise sorted, allowing us to use a binary search approach.
# We define a search space between the smallest element (matrix[0][0]) and the largest element (matrix[n-1][n-1]) in the matrix.
# We count the number of elements less than or equal to the mid-point of the search space.
# Adjust the search space based on this count until the kth smallest element is found.

# Time Complexity: O(n * log(max-min)), where n is the number of rows/columns in the matrix, 
# and max and min are the maximum and minimum elements in the matrix.
# Space Complexity: O(1) (constant space usage).
# Did this code successfully run on Leetcode: Yes.
# Any problem you faced while coding this: No.

from typing import List

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        # Helper function to count elements less than or equal to `mid`
        def countLessEqual(mid):
            count, n = 0, len(matrix)
            row, col = n - 1, 0  # Start from bottom-left corner of the matrix
            while row >= 0 and col < n:
                if matrix[row][col] <= mid:
                    # If current element <= mid, all elements in this row up to this column are <= mid
                    count += row + 1
                    col += 1
                else:
                    # Move up in the same column
                    row -= 1
            return count

        n = len(matrix)
        left, right = matrix[0][0], matrix[n-1][n-1]  # Initial binary search bounds
        
        while left < right:
            mid = left + (right - left) // 2
            if countLessEqual(mid) < k:
                left = mid + 1  # Search in the upper half
            else:
                right = mid  # Search in the lower half

        return left  # The left pointer will point to the kth smallest element
