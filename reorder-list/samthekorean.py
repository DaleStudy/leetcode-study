# TC : O(n)
# SC : O(m) m being the sum of deque and dummy nodes
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next or not head.next.next:
            return

        # Step 1: Use a deque to collect nodes
        d = deque()
        current = head
        while current:
            d.append(current)
            current = current.next

        # Step 2: Reorder the list using deque
        dummy = ListNode(0)  # Dummy node with value 0
        current = dummy
        toggle = True

        while d:
            if toggle:
                current.next = d.popleft()  # Append from the front of the deque
            else:
                current.next = d.pop()  # Append from the back of the deque
            current = current.next
            toggle = not toggle

        # Step 3: Ensure the last node points to None
        current.next = None

        # Step 4: Reassign head to point to the new reordered list
        head = dummy.next
