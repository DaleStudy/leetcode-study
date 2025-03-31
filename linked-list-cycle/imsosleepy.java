// 단순 루프 방식이 너무 오래걸려서 다른 방식을 찾아봄
public class Solution {
    public boolean hasCycle(ListNode head) {
        HashSet<ListNode> visited = new HashSet<>();
        while (head != null) {
            if (visited.contains(head)) {
                return true; // 사이클 존재
            }
            visited.add(head);
            head = head.next;
        }
        return false; // 사이클 없음
    }
}

// 투포인터로 해결
public class Solution {
    public boolean hasCycle(ListNode head) {
        if (head == null || head.next == null) return false;

        ListNode slow = head;
        ListNode fast = head;

        while (fast != null && fast.next != null) {
            slow = slow.next;        // 한 칸 이동
            fast = fast.next.next;   // 두 칸 이동

            if (slow == fast) {
                return true; // 사이클 존재
            }
        }
        return false; // 사이클 없음
    }
}
