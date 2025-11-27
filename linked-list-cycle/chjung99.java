import java.util.*;

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
    Set<ListNode> visit = new HashSet<>();
    public boolean hasCycle(ListNode head) {
        return dfs(head, visit);
    }
    public boolean dfs(ListNode head, Set<ListNode> visit){
        Deque<ListNode> stack = new ArrayDeque<>();
        if (head != null){
            visit.add(head);
            stack.push(head);
        }
        while (!stack.isEmpty()){
            ListNode cur = stack.pop();
            if (cur.next == null) continue;
            if (visit.contains(cur.next)) {
                return true;
            }
            visit.add(cur.next);
            stack.push(cur.next);
        }
        return false;
    }
}

