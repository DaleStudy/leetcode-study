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

    /**
     * 포인터 반복문을 새로 배웠을 때 fast/slow와 같은 투 포인터 알고리즘과 헷갈렸지만 둘은 전혀 다르다.
     * 포인터 반복문
     * * 링크 방향 뒤집기
     * * 3개 포인터 (prev, cur, next)
     * * 리스트 자체 구조 변경
     * <p>
     * 투 포인터
     * * 중간, 사이클, 교차점 등 탐색
     * * 2개 포인터 (slow, fast)
     * * 리스트 구조 그대로, 위치 정보만 얻음
     * <p>
     * https://bcp0109.tistory.com/142
     */
    public ListNode reverseListByPointer(ListNode head) {
        ListNode prev = null;
        ListNode cur = head;
        while (cur != null) {
            ListNode next = cur.next; // next라는 temp 변수를 사용해서 prev와 cur.next 값을 바꾼다.
            cur.next = prev;
            prev = cur;
            cur = next;
            // 대각선으로 / / / / 으로 변수명 암기하기
        }
        return prev;
    }

    public ListNode reverseListByRecursion(ListNode head) {
        // head.next가 null인지도 확인하는 로직이 필요합니다. (nullPointerException 방지)
        if (head == null || head.next == null) return null; // 재귀의 끝, 이제 기존 연산을 취합한다.
        ListNode newHead = reverseListByRecursion(head.next);
        head.next.next = head;
        head.next = null;
        return newHead;
    }
}
