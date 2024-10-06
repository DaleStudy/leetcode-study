/**
 * Floyd tortoise and hare 알고리즘을 바탕으로
 * 한칸씩 이동하는 포인터와 2칸씩 이동하는 포인터는 결국에 만난다는 점을 이용해서 품
 *
 * TC: O(N)
 * SC: O(1)
 * N: linked list length
 */

/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */

/**
 * @param {ListNode} head
 * @return {boolean}
 */
var hasCycle = function (head) {
  let oneStep = head;
  let twoStep = head;

  while (twoStep && twoStep.next) {
    if (oneStep === twoStep) {
      return true;
    }

    oneStep = oneStep.next;
    twoStep = twoStep.next.next;
  }

  return false;
};
