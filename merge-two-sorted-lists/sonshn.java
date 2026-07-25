/**
 * 재귀를 사용하여 두 개의 정렬된 연결 리스트를 병합
 * 
 * 시간 복잡도: O(n + m), n은 list1의 길이, m은 list2의 길이
 * 공간 복잡도: O(n + m), 재귀 호출로 인해 스택에 쌓이는 함수 호출의 깊이 때문
 */
class Solution {
    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
        if (list1 == null) return list2;
        if (list2 == null) return list1;

        if (list1.val <= list2.val) {
            list1.next = mergeTwoLists(list1.next, list2);
            return list1;
        } else {
            list2.next = mergeTwoLists(list1, list2.next);
            return list2;
        }
    }
}
