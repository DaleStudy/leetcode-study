# Time Complexity: O(N log N) - collecting all nodes is O(N), sorting is O(N log N)
# Space Complexity: O(N) - storing all nodes in an array

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        arr = []
        
        # collect all nodes from the linked lists
        for node in lists:
            while node:
                arr.append(node)
                node = node.next

        # sort all nodes based on their value
        arr.sort(key=lambda x: x.val)

        # reconnect nodes to form the merged linked list
        for i in range(len(arr) - 1):
            arr[i].next = arr[i + 1]

        return arr[0] if arr else None  
