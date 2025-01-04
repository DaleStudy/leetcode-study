// 처음에 여러 조건을 붙였으나 기본적인 조건만 필요하다.
// 가장 기본적인 개념은 다음에 이동할곳이 어딘지만 알려주면 됨
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
