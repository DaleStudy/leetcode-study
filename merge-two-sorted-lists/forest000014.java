/**

 (n = list1.length + list2.length)
 시간 복잡도: O(n)
 - 최악의 경우 전체 노드 순회
 공간 복잡도: O(n)
 - 최악의 경우 전체 노드만큼 새 노드 생성

 */
class Solution {
    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
        ListNode head = new ListNode();
        ListNode curr = head;

        while (true) {
            if (list1 == null) {
                curr.next = list2;
                break;
            } else if (list2 == null) {
                curr.next = list1;
                break;
            }

            if (list1.val <= list2.val) {
                curr.next = new ListNode(list1.val);
                curr = curr.next;
                list1 = list1.next;
            } else {
                curr.next = new ListNode(list2.val);
                curr = curr.next;
                list2 = list2.next;
            }
        }

        return head.next;
    }
}
