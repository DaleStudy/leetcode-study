import java.util.Stack;

class Solution {
    /**
     * 리버스와 동일한 후입선출 구조를 생각했고 그래서 자료구조로 스택을 결정했다.
     * 사이클 문제를 염두해 두고 조건을 설계했지만 사이클을 끊는 위치가 틀려서 오래 걸렸다.
     */
    public ListNode reverseList(ListNode head) {
        if (head == null) return null;

        Stack<ListNode> stack = new Stack<>();
        while (head != null) {
            stack.push(head);
            head = head.next;
        }

        ListNode newHead = stack.pop(); // 정답 반환용
        ListNode current = newHead; // 포인터를 갱신하면서 계산하기용 (소위 더미 포인터)

        while (!stack.isEmpty()) {
            current.next = stack.pop();
            current = current.next; // ← 수정: 자기 자신 가리키는 대신 앞으로 이동
        }
        current.next = null; // 마지막 tail 정리
        return newHead;
    }
}
