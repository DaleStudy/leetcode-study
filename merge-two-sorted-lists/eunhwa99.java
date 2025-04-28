public class eunhwa99 {

  // 시간 복잡도: O(n) - 두 개의 리스트를 한 번씩 순회
  // 공간 복잡도: O(1) - 추가적인 공간 사용 없음
  class Solution {
    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
      if (list1 == null) return list2;
      if (list2 == null) return list1;

      ListNode dummy = new ListNode(0);
      ListNode current = dummy;

      while (list1 != null && list2 != null) {
        if (list1.val <= list2.val) {
          current.next = list1;
          list1 = list1.next;
        } else {
          current.next = list2;
          list2 = list2.next;
        }
        current = current.next;
      }

      if (list1 != null) {
        current.next = list1;
      } else {
        current.next = list2;
      }

      return dummy.next;
    }
  }
}

