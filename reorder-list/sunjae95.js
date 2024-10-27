/**
 * @description
 * 인덱스로 접근하지 못하는 구조를 인덱스로 접근하게 하여 two pointer로 풀이
 *
 * n = total node count
 * time complexity: O(n)
 * space complexity: O(n)
 */
var reorderList = function (head) {
  // convert from queue to list
  let travelNode = head;
  const list = [];
  while (travelNode) {
    list.push(travelNode);
    travelNode = travelNode.next;
  }
  // two pointer
  let [left, right] = [0, list.length - 1];
  const node = new ListNode();
  let tail = node;

  while (left <= right) {
    // 1. left append
    const leftNode = list[left];
    leftNode.next = null;
    tail.next = leftNode;
    tail = leftNode;
    // 2. conditional right append
    const rightNode = list[right];
    rightNode.next = null;
    if (left !== right) {
      tail.next = rightNode;
      tail = rightNode;
    }

    left++;
    right--;
  }

  head = node.next;
};
