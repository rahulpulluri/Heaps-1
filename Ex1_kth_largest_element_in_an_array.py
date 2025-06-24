# Intuition:
# We are given an unsorted array and need to find the k-th largest element.
#
# A brute force approach is to sort the array and pick the (k-1)-th index — but this takes O(n log n) time.
# A better approach is to use a Max Heap and pop the largest k times — but this uses O(n) space.
#
# The optimal approach for consistent performance is to use a Min Heap of size k:
# - We push elements one by one into the heap
# - If the heap grows beyond k, we remove the smallest
# - In the end, the top of the heap is the k-th largest element
#
# If average-case performance is a higher priority than worst-case, Quickselect offers O(n) time on average.
# However, Quickselect has a worst-case of O(n²) and slightly more complex logic.
#
# So we choose the Min Heap for reliable behavior in all scenarios.

# ----------------------------------------------------
# Time Complexity: O(n log k)
# - Push each of the n elements into the heap: O(log k) per push
# - If heap size > k, pop takes O(log k)
#
# Space Complexity: O(k)
# - Min Heap of at most k elements
# ----------------------------------------------------

import heapq
import random
from typing import List

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for num in nums:
            heapq.heappush(heap, num)
            if len(heap) > k:
                heapq.heappop(heap)
        return heap[0]
    

# ------------------------------------------------------
# Quickselect Approach (Randomized Recursive Partition)
#
# Time Complexity: O(n) average, O(n²) worst case
# Space Complexity: O(n) due to slicing (can be improved with in-place version)
#
# Intuition:
# - Randomly choose a pivot and partition elements into:
#   > left: greater than pivot
#   > mid: equal to pivot
#   > right: less than pivot
# - Recursively search in the segment that contains the k-th largest

#         def quick_select(nums, k):
#             pivot = random.choice(nums)
#             left, mid, right = [], [], []
#             for num in nums:
#                 if num > pivot:
#                     left.append(num)
#                 elif num < pivot:
#                     right.append(num)
#                 else:
#                     mid.append(num)
#             if k <= len(left):
#                 return quick_select(left, k)
#             elif k > len(left) + len(mid):
#                 return quick_select(right, k - len(left) - len(mid))
#             else:
#                 return pivot
#         return quick_select(nums, k)

# ------------------------------------------------------

# Max Heap Approach (Simulate Max Heap using Negatives)
#
# Time Complexity: O(n + k log n)
# Space Complexity: O(n)
#
# Intuition:
# - Push all elements as negatives to simulate max heap
# - Pop k times to reach the k-th largest

#         max_heap = [-num for num in nums]
#         heapq.heapify(max_heap)
#         for _ in range(k):
#             val = -heapq.heappop(max_heap)
#         return val


# ------------------------------------------------------
# Brute Force Approach (Sort the Array)
#
# Time Complexity: O(n log n)
# Space Complexity: O(1) or O(n) depending on sorting implementation
#
# Intuition:
# - Sort the array in descending order
# - Return the k-th element

#         nums.sort(reverse=True)
#         return nums[k - 1]
