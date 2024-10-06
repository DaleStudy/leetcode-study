import java.util.List;

//  Definition for singly-linked list.
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
    var list1 = new ListNode(1);
    list1.next = new ListNode(2);
    list1.next.next = new ListNode(4);

    var list2 = new ListNode(1);
    list2.next = new ListNode(3);
    list2.next.next = new ListNode(4);

    System.out.println(s.mergeTwoLists(list1, list2));
  }

  public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
    // A와 B 헤드를 비교
    // A가 더 작거나 같으면 A 헤드를 빼서 새 노드로 추가
    // 그렇지 않으면 B 헤드를 빼서 새 노드로 추가
    // TC: O(N+M), N: list1의 길이, M: list2의 길이
    // SC: O(N+M), N: list1의 길이, M: list2의 길이
    ListNode mergedList = null;

    while(list1 != null && list2 != null) {
      if (list1.val <= list2.val) {
        mergedList = addNode(mergedList, list1.val);
        list1 = list1.next;
      } else {
        mergedList = addNode(mergedList, list2.val);
        list2 = list2.next;
      }
    }

    while(list1 != null) {
      mergedList = addNode(mergedList, list1.val);
      list1 = list1.next;
    }

    while(list2 != null) {
      mergedList = addNode(mergedList, list2.val);
      list2 = list2.next;
    }

    return mergedList;
  }

  private ListNode addNode(ListNode node, int val) {
    if (node == null) {
      node = new ListNode(val);
    } else {
      var last = node;
      while(last.next != null) {
        last = last.next;
      }
      last.next = new ListNode(val);
    }

    return node;
  }
}
