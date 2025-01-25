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

// 시간 복잡도 : O(n)
// 공간 복잡도 : O(n)
class Solution {
	public ListNode reverseList(ListNode head) {
		// 반복문을 돌면서 f(x+1)의 next를 f(x)로 지정
		ListNode result = null;

		while(head != null) {
			ListNode nextNode = new ListNode(head.val);
			nextNode.next = result;
			result = nextNode;
			head = head.next;
		}

		return result;
	}
}


