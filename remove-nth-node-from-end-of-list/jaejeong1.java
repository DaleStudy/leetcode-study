import java.util.LinkedList;

// Definition for singly-linked list.
class ListNode {
  int val;
  ListNode next;
  ListNode() {}
  ListNode(int val) { this.val = val; }
  ListNode(int val, ListNode next) { this.val = val; this.next = next; }
}

class Solution {

  public static void main(String[] args) {
    Solution s = new Solution();
    var node = new ListNode(1, new ListNode(2));
    s.removeNthFromEnd(node, 1);
  }

  public ListNode removeNthFromEnd(ListNode head, int n) {
    // 문제: 링크드리스트의 head가 주어지면 끝에서 N번째 노드를 삭제한 결과를 반환하라
    // 풀이: n번째만큼 first 이동, 그 후 second를 1칸씩 함께 이동 시킨다 first가 끝에 도달할 때 까지
    // 전체 길이 L, 주어진 N이 있을때 이렇게 하면 L - N - 1 위치를 구할 수 있다.
    // TC: O(N)
    // SC: O(1)
    var dummy = new ListNode(-1, head);
    var first = head;
    for (int i=0; i<n; i++) {
      first = first.next;
    }

    var second = dummy;

    while(first != null) {
      first = first.next;
      second = second.next;
    }

    second.next = second.next.next;
    return dummy.next;
  }

}
