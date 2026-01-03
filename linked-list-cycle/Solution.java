
class ListNode {
  int val;
  ListNode next;

  ListNode(int x) {
    val = x;
    next = null;
  }
}

public class Solution {

  /**
   * floyd 알고리즘(토끼 거북) 알고리즘 사용해서
   * 무한한 순환을 찾기
   */
  public boolean hasCycle(ListNode head) {
    if (head == null)
      return false;

    ListNode rb = head;
    ListNode tt = head;
    // 토끼와 거북이의 주소가 동일할 때까지 탐색하기
    while (rb.next != null && rb.next.next != null) {
      // 토끼는 두 노드씩 이동하기
      rb = rb.next.next;
      // 거북이는 한 노드씩 이동하기
      tt = tt.next;
      if (rb == tt) {
        // System.out.println("토끼("+rb.val+")와 거북이("+tt.val+")가 만났음");
        return true;
      }
    }
    return false;
  }
}
