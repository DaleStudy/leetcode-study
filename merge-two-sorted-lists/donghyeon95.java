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
	public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
		// O(N)
		// 2포인터로 지나가용 하면 되는 문제
		ListNode result = new ListNode();
		ListNode nowNode = result;


		while (list1!=null || list2!=null) {
			int first = list1==null? 101: list1.val;
			int second = list2==null? 101: list2.val;

			if (first < second) {
				nowNode.next = new ListNode(first);
				nowNode = nowNode.next;
				list1 = list1.next;
			} else {
				nowNode.next = new ListNode(second);
				nowNode = nowNode.next;
				list2 = list2.next;
			}
		}

		return result.next;
	}
}

