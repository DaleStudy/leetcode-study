
class Solution {
    public void reorderList(ListNode head) {
        if(head.next == null) return;

        ListNode prev = null;
        while (true) {
            ListNode tail = head;
            while (tail.next != null) {
                prev = tail;
                tail = tail.next;
            }
            
            if (prev == head) break;  
            
            // tail 이동
            ListNode headNext = head.next;
            prev.next = null;
            head.next = tail;
            tail.next = headNext;
            
            head = headNext;
        }
    }
}
