//Definition for singly-linked list.
class ListNode {
  int val;
  ListNode next;
  ListNode(int x) {
    val = x;
    next = null;
  }
}

class Solution {
  public boolean hasCycle(ListNode head) {
    // 풀이 1: Set에 객체를 집어 넣고, 사이즈가 안늘어나면 사이클이 있다고 판단할 수 있다
    // TC: O(N)
    // SC: O(N)
//    Set<ListNode> set = new HashSet<>();
//
//    while(head != null) {
//      var before = set.size();
//      set.add(head);
//      var after = set.size();
//      if (before == after) {
//        return true;
//      }
//      head = head.next;
//    }
//
//    return false;

    // 풀이 2: 두개의 포인터를 사용해 첫번째 포인터는 하나씩, 두번째 포인터는 두개씩 순환하다 겹치는 부분이 생기면 순환이라고 판단할 수 있다
    // TC: O(N)
    // SC: O(1)
    var slow = head;
    var fast = head;
    while (fast != null && fast.next != null) {
      slow = slow.next;
      fast = fast.next.next;

      if (slow == fast) {
        return true;
      }
    }

    return false;
  }
}
