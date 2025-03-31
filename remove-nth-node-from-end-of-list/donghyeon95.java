import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Queue;

/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
	public ListNode removeNthFromEnd(ListNode head, int n) {
		ArrayList<ListNode> list = new ArrayList<>();
		ListNode nhead = head;

		while (nhead != null) {
			list.add(nhead);
			nhead = nhead.next;
		}

		int size = list.size();

		if (size == n) {
			return head.next;
		}

		list.get(size - n - 1).next = list.get(size - n).next;

		return head;
	}
}

