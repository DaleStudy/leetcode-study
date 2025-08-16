/**
 * 고생한 이유: ListNode 의 시작점을 따로 둬야 하는 것!
 * 
 * ListNode dummy = new ListNode(0); // 시작점
 * ListNode output = dummy; // 시작점 뒤에 실제 작업용 포인터
 * 
 * 
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public static ListNode mergeTwoLists(ListNode list1, ListNode list2) {
        // 길이가 둘다 null 이면, return null
        if (list1 == null && list2 == null) return null;

        ListNode dummy = new ListNode(0); // 시작점
        ListNode output = dummy; // 시작점 뒤에 실제 작업용 포인터

        while(list1 != null && list2 != null) {

            if (list1.val < list2.val) {
                output.next = list1;
                list1 = list1.next;  // list1 포인터 이동
            } else {
                output.next = list2;
                list2 = list2.next;  // list2 포인터 이동
            }
            output = output.next; // output 포인터 이동
        }

        if (list1 != null) {
            output.next = list1;
        }
        if (list2 != null) {
            output.next = list2;
        }

        return dummy.next;
    }
}
