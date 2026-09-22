/**
 * TC : O(n)
 * - 전체 리스트를 한번 순회 하므로 O(n)
 * SC : O(1)
 * - 임시 변수 하나만 사용하므로 O(1)
 */
class Solution {
    public ListNode reverseList(ListNode head) {
        ListNode prev = null;

        while(head != null) {
            ListNode next = head.next; // 다음 순서의 노드
            head.next = prev; // 현재 노드의 다음을 이전 노드로
            prev = head;      // 다음 차례의 이전 노드는 현재
            head = next;      // 다음 차례는 임시 저장했던 노느
        }
        return prev;
    }
}
