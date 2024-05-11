/**
 * 순환 리스트
 * 달레님 강의 참고
 * 기존에 이해했던 Linked List 처럼 null이 되는 경우가 아니기 때문에 loop에 빠지지 않게 주의해야 한다.
 * 시간복잡도: O(n)
 * 공간복잡도: O(n)
 */
class Solution {
    public boolean hasCycle(ListNode head) {
        Set<ListNode> visited = new HashSet<>();
        while (head != null) {
            if (visited.contains(head)) {
                return true;
            } else {
                visited.add(head);
                head = head.next;
            }
        }

        return false;
    }
}
