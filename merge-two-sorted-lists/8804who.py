# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        sorted_list = []

        while True:
            if list1 is None and list2 is None:
                break
            elif list1 is None:
                sorted_list.append(list2.val)
                list2 = list2.next
            elif list2 is None:
                sorted_list.append(list1.val)
                list1 = list1.next
            else:
                if list1.val > list2.val:
                    sorted_list.append(list2.val)
                    list2 = list2.next
                else:
                    sorted_list.append(list1.val)
                    list1 = list1.next
        
        def get_node(idx):
            if idx < len(sorted_list):
                return ListNode(sorted_list[idx], get_node(idx+1))
            else:
                return None

        answer= get_node(0)

        return answer
    
