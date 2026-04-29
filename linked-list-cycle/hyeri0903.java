/**
 * Definition for singly-linked list.
 * class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
public class Solution {
    public boolean hasCycle(ListNode head) {
        /**
        1.prob: linked list 이면 true, 아니면 false return
        2.constraints
        - # of nodes min = 0, max = 10000
        - pos: -1 or valid index
        - pos는 파라미터로 받지 않음
        3.solution
        - pointer 2개를 두고 1개는 2칸씩, 1개는 1칸씩 이동하며 결국 만나는지 체크
        만나면 true, 안 만나면 false return
         */

         ListNode slow = head;
         ListNode fast = head;

        while(fast != null && fast.next != null) {
            slow = slow.next;
            fast = fast.next.next;

            //노드가 동일하면 linked list
            if(slow == fast) {
                return true;
            }
        }
        return false;
        
    }
}
