
/* 
첫 번째 풀이
class Solution {
    public ListNode removeNthFromEnd(ListNode head, int n) {
        List<ListNode> list = new ArrayList<>();
        
        while(head != null) {
            list.add(head);
            head = head.next;
        }

        list.remove(list.size()-n);
        if (list.isEmpty()) return null;

        for (int i = 0; i < list.size()-1; i++) {
            list.get(i).next = list.get(i+1);
        }
        list.get(list.size()-1).next = null;
        return list.get(0);
    }
}
*/


/* 
시간 복잡도: O(N)
공간 복잡도: O(1)

class Solution {
    public ListNode removeNthFromEnd(ListNode head, int n) {
        ListNode dummy = new ListNode(0);
        dummy.next = head;

        ListNode fast = dummy;
        ListNode slow = dummy;
        
        for (int i = 0; i <= n; i++) {
            fast = fast.next;
        }

        while(fast != null) {
            fast = fast.next;
            slow = slow.next;
        }

        slow.next = slow.next.next;

        return dummy.next;
    }
}
*/

/**
 * 
 * 시간 복잡도는 O(n)
 * 공간 복잡도는 O(1)
 */
class Solution {
    public ListNode removeNthFromEnd(ListNode head, int n) {
        int length = 0;
        ListNode curLenCheck = head;

        while(curLenCheck != null) {
            length++;
            curLenCheck = curLenCheck.next;
        }

        int targetIndex = length - n;
        if (targetIndex == 0) return head.next;

        ListNode targetPrev = head;
        for (int i=0; i < targetIndex-1; i++) {
            targetPrev = targetPrev.next;
        }
        targetPrev.next = targetPrev.next.next;

        return head;
    }
}
