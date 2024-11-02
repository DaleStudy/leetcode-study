/**
 * 2차
 * n만큼 first가 움직인 다음, first가 끝까지 갈때까지 second를 움직입니다.
 * 그럼 그 위치가 끝에서 n번째임을 알 수 있는 풀이입니다.
 *
 * TC: O(N)
 * SC: O(1)
 * N: list length
 */

/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @param {number} n
 * @return {ListNode}
 */
var removeNthFromEnd = function (head, n) {
  const resultHead = new ListNode(null, head);
  let first = resultHead;
  let second = resultHead;

  while (n > 0) {
    first = first.next;
    n -= 1;
  }

  while (first.next) {
    first = first.next;
    second = second.next;
  }

  second.next = second.next.next;

  return resultHead.next;
};

/**
 * 1차
 * 전체 순회로 갯수를 파악하고 해당 위치로가서 링크 연결 수정 작업
 *
 * TC: O(N)
 * SC: O(1)
 * N: list length
 */

/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @param {number} n
 * @return {ListNode}
 */
var removeNthFromEnd = function (head, n) {
  let listLength = 0;
  let pointer = head;

  while (pointer) {
    pointer = pointer.next;
    listLength += 1;
  }

  // if target of removal is the first node in list
  if (listLength === n) {
    return head.next;
  }

  let nextCount = listLength - n - 1;
  pointer = head;

  while (nextCount) {
    pointer = pointer.next;
    nextCount -= 1;
  }

  pointer.next = pointer.next.next;

  return head;
};
