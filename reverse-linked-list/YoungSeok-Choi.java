import java.util.HashMap;
import java.util.Map;

/**
 * Definition for singly-linked list.
 * public class ListNode {
 * int val;
 * ListNode next;
 * ListNode() {}
 * ListNode(int val) { this.val = val; }
 * ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode reverseList(ListNode head) {
        int idx = 0;
        Map<Integer, Integer> idxMap = new HashMap<>();

        if (head == null || head.next == null) {
            return null;
        }

        while (true) {
            idxMap.put(idx++, head.val);

            if (head.next == null) {
                break;
            }

            head = head.next;
        }

        ListNode resHead = new ListNode();
        ListNode cur = resHead;

        for (int i = idx - 1; i >= 0; i--) {
            cur.val = idxMap.get(i);

            if (i != 0) {
                cur.next = new ListNode();
                cur = cur.next;
            }
        }

        return resHead;
    }

}

// O(n) + 변수 하나로 직관적으로 문제를 해결할 수 있다..
class AnotherSolution {
    public ListNode reverstList(ListNode head) {
        ListNode prev = null;
        ListNode cur = head;

        while (cur.next != null) {
            ListNode next = cur.next;
            cur.next = prev;
            prev = cur;
            cur = next;
        }

        return prev;
    }
}

class ListNode {
    int val;
    ListNode next;

    ListNode() {
    }

    ListNode(int val) {
        this.val = val;
    }

    ListNode(int val, ListNode next) {
        this.val = val;
        this.next = next;
    }
}
