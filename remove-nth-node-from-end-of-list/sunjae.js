/**
 * @description
 * 전체 노드의 길이를 구한 뒤 n에 적합한 노드만 건너뛰어 노드를 재배열 시켜줌
 *
 * n = total length of head node list
 * time complexity: O(n)
 * space complexity: O(n)
 */
var removeNthFromEnd = function (head, n) {
  let node;
  let nodeCount = 0;

  node = head;
  while (node) {
    nodeCount++;
    node = node.next;
  }

  let answer = new ListNode();
  let answerNode = answer;

  node = head;
  for (let i = 0; i < nodeCount; i++) {
    if (nodeCount - n === i) {
      i++;
      node = node.next;
    }

    answerNode.next = node;
    answerNode = node;

    node = node?.next ?? null;
  }

  return answer.next;
};
