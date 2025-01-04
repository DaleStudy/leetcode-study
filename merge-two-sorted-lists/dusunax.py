'''
# 21. Merge Two Sorted Lists

A. iterative approach: use a two pointers to merge the two lists.
B. recursive approach: use recursion to merge the two lists.


## Time and Space Complexity

### A. Iterative Approach

```
TC: O(n + m)
SC: O(1)
```

#### TC is O(n + m):
- iterating through the two lists just once for merge two sorted lists. = O(n + m)

#### SC is O(1):
- temp node is used to store the result. = O(1)

### B. Recursive Approach

```
TC: O(n + m)
SC: O(n + m)
```

#### TC is O(n + m):
- iterating through the two lists just once for merge two sorted lists. = O(n + m)

#### SC is O(n + m):
- because of the recursive call stack. = O(n + m)
'''
class Solution:
    '''
    A. Iterative Approach
    - use a temp node to store the result.
    - use a current node to iterate through the two lists.
    '''
    def mergeTwoListsIterative(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        temp = ListNode(-1)
        current = temp

        while list1 is not None and list2 is not None:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next
        
        if list1 is not None:
            current.next = list1
        elif list2 is not None:
            current.next = list2

        return temp.next

    '''
    B. Recursive Approach
    - use recursion to merge the two lists.
    '''
    def mergeTwoListsRecursive(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None:
            return list2
        elif list2 is None:
            return list1

        if list1.val < list2.val:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        else:
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2
