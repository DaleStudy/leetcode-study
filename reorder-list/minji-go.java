/**
 * <a href="https://leetcode.com/problems/reorder-list/">week11-2. reorder-list</a>
 * <li>Description: Reorder the list to be on the following form: L0 → Ln → L1 → Ln - 1 → L2 → ... </li>
 * <li>Topics: Linked List, Two Pointers, Stack, Recursion </li>
 * <li>Time Complexity: O(N), Runtime 5ms       </li>
 * <li>Space Complexity: O(N), Memory 47.96MB   </li>
 */
class Solution {
    public void reorderList(ListNode head) {
        Deque<ListNode> deque = new ArrayDeque<>();

        ListNode node = head;
        while (node != null) {
            deque.addLast(node);
            node = node.next;
        }

        ListNode curr = deque.removeFirst();
        while (!deque.isEmpty()) {
            curr.next = deque.removeLast();
            curr = curr.next;
            if (!deque.isEmpty()) {
                curr.next = deque.removeFirst();
                curr = curr.next;
            }
        }
        curr.next = null;
    }
}
