/**
 * TC : O(n)
 *   - 전체 리스트를 한번 순회하므로 O(n)
 * SC : O(n)
 *   - 최대 n개의 노드를 Set에 저장하므로 O(n)
 */
public class Solution {
    public boolean hasCycle(ListNode head) {
        Set<ListNode> seen = new HashSet<>();
        for(ListNode cur = head; cur !=null; cur = cur.next) {
            if(!seen.add(cur)) return true;
        }
        return false;
    }
}

/**
 * TC : O(n)
 *   - fast가 slow를 따라잡을 때까지 최악의 경우 2n번 노드를 순회하고, slow는 n번 순회하므로 O(n)
 * SC : O(1)
 *   -  slow, fast가 모두 포인터만을 사용하므로 O(1)
 */
public class Solution {
    public boolean hasCycle(ListNode head) {
        ListNode slow = head;   
        ListNode fast = head;

        while(fast != null && fast.next != null) {
            slow = slow.next; 
            fast = fast.next.next;

            if(slow == fast) {
                return true;
            }
        }
        return false;
    }
}
