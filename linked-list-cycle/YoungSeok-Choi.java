import java.util.ArrayList;
import java.util.HashMap;
import java.util.HashSet;
import java.util.List;
import java.util.Map;
import java.util.Set;

public class Solution {
    public boolean hasCycle(ListNode head) {
        Set<ListNode> nSet = new HashSet<>();

        while (head != null) {
            if (nSet.contains(head)) {
                return true;
            }

            nSet.add(head);
            head = head.next;
        }

        return false;
    }
}

/**
 * Definition for singly-linked list.
 * class ListNode {
 * int val;
 * ListNode next;
 * ListNode(int x) {
 * val = x;
 * next = null;
 * }
 * }
 */
// NOTE: 같은 val의 다른 Node의 경우를 고려하지 못했다
class WrongSolution {
    public boolean hasCycle(ListNode head) {
        Map<Integer, List<Integer>> vMap = new HashMap<>(); // NOTE: val, pos

        if (head == null) {
            return false;
        }

        ListNode cur = head;
        boolean isCyclick = false;
        int pos = -1;
        while (cur != null) {

            if (vMap.containsKey(cur.val)) {
                isCyclick = true;
                break;
            }

            List<Integer> posList = new ArrayList<>();
            posList.add(pos++);
            vMap.put(cur.val, posList);
            cur = head.next;
        }

        if (isCyclick) {
            return true;
        } else {
            return false;
        }
    }
}
