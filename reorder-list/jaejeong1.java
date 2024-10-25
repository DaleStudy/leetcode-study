import java.util.Stack;

// Definition for singly-linked list.
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

class Solution {

  public void reorderList(ListNode head) {
    // 풀이: 역순으로 저장할 스택에 node들을 넣고, 기존 node 1개/스택 node 1개씩 이어 붙인다
    // 스택은 LIFO로 저장되기 때문에, 문제에서 요구하는 순서대로 reorderList를 만들 수 있다
    // TC: O(N)
    // SC: O(N)
    Stack<ListNode> stack = new Stack<>();

    var curNode = head;
    while(curNode != null) {
      stack.push(curNode);
      curNode = curNode.next;
    }

    curNode = head;
    var halfSize = stack.size() / 2; // 한번에 2개씩 연결하기때문에 절반까지만 돌면 됨
    for (int i=0; i<halfSize; i++) {
      var top = stack.pop();

      var nextNode = curNode.next;
      curNode.next = top;
      top.next = nextNode;

      curNode = nextNode;
    }

    // 만약 노드의 개수가 홀수면, 하나의 노드가 남기 때문에 next 노드를 null로 처리해줘야 한다.
    if (curNode != null) {
      curNode.next = null;
    }
  }
}
