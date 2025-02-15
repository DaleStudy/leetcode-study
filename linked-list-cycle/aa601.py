'''
    TC : O(n)
    SC : O(n)
'''
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        tmp = head
        visited = set()
        while tmp:
            if tmp in visited:
                return True
            visited.add(tmp)
            tmp = tmp.next
        return False
