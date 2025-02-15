// 이전 노드의 헤드와 현재노드 헤드를 하나씩 이동하면서 교환하면 자연스럽게 연결리스트가 뒤집힌다.
// 각 노드를 한번씩 방문하므로 O(N)의 시간복잡도를 갖는다.
class Solution {
    public ListNode reverseList(ListNode head) {
        ListNode prev = null;
        ListNode current = head;

        while (current != null) {
            ListNode nextNode = current.next;
            current.next = prev;
            prev = current;
            current = nextNode;
        }

        return prev;
    }
}
