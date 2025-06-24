# Intuition:
# We are given k sorted linked lists and need to merge them into a single sorted linked list.
#
# A naive idea is to collect all node values, sort them, and rebuild a new list (Brute Force).
# A better idea is to merge one list at a time, similar to merging arrays (One-by-One Merge).
# The most optimal solution uses a Min Heap to always select the smallest node among the current heads,
# ensuring minimal work per node and logarithmic overhead based on k lists.

# ----------------------------------------------------
# Time Complexity: O(N * log k)
# - N = total number of nodes in all lists
# - k = number of linked lists
# - Each node is pushed/popped from the heap once → log k per operation
#
# Space Complexity: O(k) for the heap
# - Output list reuses existing nodes → no extra list creation
# ----------------------------------------------------

import heapq
from typing import List, Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        for i, node in enumerate(lists):
            if node:
                heapq.heappush(heap, (node.val, i, node))

        dummy = ListNode()
        curr = dummy

        while heap:
            val, i, node = heapq.heappop(heap)
            curr.next = node
            curr = curr.next
            if node.next:
                heapq.heappush(heap, (node.next.val, i, node.next))

        return dummy.next


# ------------------------------------------------------
# One-by-One Merge Approach
#
# Time Complexity: O(N * k) in worst case, where each of the k-1 merges takes up to N time
# Space Complexity: O(1)
#
# Intuition:
# - Start with the first list
# - Merge it with the next one, repeat until all lists are merged
# - Inefficient for large k due to repeated full traversals

#         if not lists or len(lists) == 0:
#             return None
#
#         def mergeTwoList(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
#             dummy = ListNode()
#             curr = dummy
#             while l1 and l2:
#                 if l1.val < l2.val:
#                     curr.next = l1
#                     l1 = l1.next
#                 else:
#                     curr.next = l2
#                     l2 = l2.next
#                 curr = curr.next
#             curr.next = l1 if l1 else l2
#             return dummy.next
#
#         res = lists[0]
#         for i in range(1, len(lists)):
#             res = mergeTwoList(res, lists[i])
#         return res


# ------------------------------------------------------
# Brute Force Approach (Collect All Values and Sort)
#
# Time Complexity: O(N log N) where N is total nodes
# Space Complexity: O(N) to store all values before rebuilding list
#
# Intuition:
# - Extract all values into an array
# - Sort the array
# - Create a new linked list from the sorted values

#         nodes = []
#         head = point = ListNode(0)
#         for l in lists:
#             while l:
#                 nodes.append(l.val)
#                 l = l.next
#         for x in sorted(nodes):
#             point.next = ListNode(x)
#             point = point.next
#         return head.next
