public class Solution {
    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
        //1. null 체크
        if(list1 == null || list2 == null) {
            return list1 != null ? list1 : list2;
        }
        //1. 값 비교
        if(list1.val < list2.val) {
            //다음 Node 비교
            list1.next = mergeTwoLists(list1.next, list2);
            return list1;
        } else {
            list2.next = mergeTwoLists(list1, list2.next);
            return list2;
        }
    }
}
