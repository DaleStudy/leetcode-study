/**
 * time: O(N)
 * space: O(N)
 */
class Solution {

    public void reorderList(ListNode head) {
        if (head.next == null) {
            return;
        }
        ListNode reorderHead = head;
        List<ListNode> nodes = new ArrayList<>();
        while (head != null) {
            ListNode next = head.next;
            head.next = null;
            nodes.add(head);
            head = next;
        }

        int left = 0;
        int right = nodes.size() - 1;
        while (left < right) {
            reorderHead.next = nodes.get(right);
            right--;
            left++;
            if (left <= right && left < nodes.size()) {
                reorderHead = reorderHead.next;
                reorderHead.next = nodes.get(left);
                reorderHead = reorderHead.next;
            }
        }
    }
}
