from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low, high = 0, len(nums) - 1

        while low <= high:
            mid = (low + high) // 2

            if nums[mid] == target:
                return mid

            # Check which half of the array is sorted and perform binary search accordingly
            if nums[low] <= nums[mid]:  # Left half is sorted
                if nums[low] <= target < nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            else:  # Right half is sorted
                if nums[mid] < target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1
        return -1  # Target not found
    

# Input: sorted_list is a list of integers
sorted_list = [int(x) for x in input("Enter sorted list elements separated by spaces: ").split()]

# Input: target_element is an integer
target_element = int(input("Enter the target element: "))

# Create an instance of the Solution class
solution = Solution()

# Call the search method to find the position of the target_element
position = solution.search(sorted_list, target_element)

if position != -1:
    print(f"{target_element} found at index {position}")
else:
    print(f"{target_element} not found")
