/**
    길이가 최대 10000이므로 10001까지 경우의 수를 돌아 확인하는 방법
 */
public class Solution {
    public boolean hasCycle(ListNode head) {
        int max = 10001;
        int idx = 0;
        boolean result = false;
        while(head != null) {
            idx++;
            head = head.next;
            if(idx > max) {
                result = true;
                break;
            }
        }

        return result;
    }
}
/**
    2개의 포인터를 이용하여, 만나는지 확인하는 방법
 */
public class Solution2 {
    public boolean hasCycle(ListNode head) {
        ListNode first = head;
        ListNode second = head;
        boolean result = false;
        while(second != null && second.next != null) {
            first = first.next;
            second = second.next.next;
            if(first == second) {
                result = true;
                break;
            }
        }

        return result;
    }
}
