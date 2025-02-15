class Solution {
    public ListNode reverseList(ListNode head) {
        // while 풀이
        // 시간복잡도 : O(n), 공간복잡도 : O(1)
        // 핵심 : node에 순서대로 null <- 1 <- 2 <- 3 담는 과정이 필요
        // node = null로 시작하고, 다음 값을 temp에 넣어둔 뒤 순서대로 값 변경
        ListNode node = null;

        while (head != null) {
            ListNode temp = head.next;
            head.next = node;
            node = head;
            head = temp;
        }

        return node;
    }
}
