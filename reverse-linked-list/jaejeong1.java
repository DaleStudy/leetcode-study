
//Definition for singly-linked list.
class ListNode {
  int val;
  ListNode next;
  ListNode() {}
  ListNode(int val) { this.val = val; }
  ListNode(int val, ListNode next) { this.val = val; this.next = next; }
}

class SolutionReverseLinkedList {
  public ListNode reverseList(ListNode head) {
    // 풀이: 링크드리스트 방향을 현재 기준으로 뒤집고, 노드를 다음으로 옮기며 반복한다
      // next = curr.next
      // prev > curr
      // prev < curr
      // prev = curr
      // curr = next
    // TC: O(N), head 길이 N만큼
    // SC: O(1), prev/curr 2개만 메모리 사용

    ListNode prev = null;
    ListNode curr = head;
    while(curr != null) {
      ListNode next = curr.next;
      curr.next = prev;
      prev = curr;
      curr = next;
    }

    return prev;
  }
}
