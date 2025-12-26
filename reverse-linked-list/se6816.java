/**
    리스트의 길이 -> N
    시간 복잡도 : O(N)
    공간 복잡도 : O(1)
*/
class Solution {
    public ListNode reverseList(ListNode head) {
        return createReverseHead(head);
    }
    private ListNode createReverseHead(ListNode head) {
        ListNode resultHead = null;

        while (head != null) {
            ListNode next = head.next; 
            head.next = resultHead;       
            resultHead = head;            
            head = next;     
        }

        return resultHead;
    }
}
