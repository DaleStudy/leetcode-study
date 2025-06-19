/**
 * <a href="https://leetcode.com/problems/https://leetcode.com/problems/merge-k-sorted-lists/">week10-5. merge-k-sorted-lists</a>
 * <li>Description: Merge all the linked-lists into one sorted linked-list          </li>
 * <li>Topics: Linked List, Divide and Conquer, Heap (Priority Queue), Merge Sort   </li>
 * <li>Time Complexity: O(NlogK), Runtime 1ms   </li>
 * <li>Space Complexity: O(K), Memory 44.7MB   </li>
 */
class Solution {
    public ListNode mergeKLists(ListNode[] lists) {
        if (lists == null || lists.length == 0) {
            return null;
        }
        return mergeKLists(lists, 0, lists.length - 1);
    }

    private ListNode mergeKLists(ListNode[] lists, int start, int end) {
        if (start == end) {
            return lists[start];
        }

        int mid = (start + end) / 2;
        ListNode node1 = mergeKLists(lists, start, mid);
        ListNode node2 = mergeKLists(lists, mid + 1, end);
        return mergeTwoLists(node1, node2);
    }

    private ListNode mergeTwoLists(ListNode node1, ListNode node2) {
        ListNode dummy = new ListNode(-10_001);
        ListNode merge = dummy;

        while (node1 != null && node2 != null) {
            if (node1.val < node2.val) {
                merge.next = node1;
                merge = merge.next;
                node1 = node1.next;
            } else {
                merge.next = node2;
                merge = merge.next;
                node2 = node2.next;
            }
        }

        if (node1 != null && node2 == null) {
            merge.next = node1;
        } else {
            merge.next = node2;
        }

        return dummy.next;
    }
}
