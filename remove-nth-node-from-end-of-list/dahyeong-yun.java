/**
 * TC: O(n)
 *   - ListNode의 길이 n 만큰 순회하므로 O(n)
 * SC: O(n)
 *   - ListNode의 길이 n 만큼 ArrayList 할당하므로 O(n)
 */
class Solution {
    public ListNode removeNthFromEnd(ListNode head, int n) {
        List<ListNode> list = new ArrayList<>();
        ListNode cursor = head.next;
        list.add(head);

        while (cursor != null) {
            list.add(cursor);
            cursor = cursor.next;
        }

        int sz = list.size();
        int deleteTarget = list.size() - n;
        if (deleteTarget < 0)
            return null;

        if (deleteTarget - 1 >= 0 && deleteTarget <= sz - 2) {
            list.get(deleteTarget - 1).next = list.get(deleteTarget + 1);
        } else if(deleteTarget == 0) {
            head = head.next;
        } else {
            list.get(deleteTarget - 1).next = null;
        }
        return head;
    }
}
