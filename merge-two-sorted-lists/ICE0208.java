class Solution {
    /**
     * 두 정렬된 연결 리스트의 기존 노드를 재사용하여 하나의 정렬된 리스트로 병합한다.
     *
     * 시간 복잡도: O(n + m)
     * - n: list1의 길이
     * - m: list2의 길이
     *
     * 공간 복잡도: O(1)
     * - 새로운 노드를 생성하지 않고 기존 노드를 재사용한다.
     */
    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
        ListNode dummyHead = new ListNode();
        ListNode tail = dummyHead;

        // 두 리스트를 순회하며 더 작은 노드를 결과 리스트의 뒤에 연결한다.
        while (list1 != null && list2 != null) {
            if (list1.val <= list2.val) {
                tail.next = list1;
                list1 = list1.next;
            } else {
                tail.next = list2;
                list2 = list2.next;
            }

            tail = tail.next;
        }

        // 한쪽 리스트가 끝나면 다른 리스트의 남은 노드들을 그대로 연결한다.
        tail.next = list1 != null ? list1 : list2;

        return dummyHead.next;
    }
}
