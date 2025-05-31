public class sora0319 {
    public class Solution {
        public boolean hasCycle(ListNode head) {
            ListNode back = head;
            ListNode front = head;

            while (front != null && front.next != null) {
                back = back.next;
                front = front.next.next;

                if (back == front) {
                    return true;
                }
            }

            return false;
        }
    }
}

