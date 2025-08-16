/**
 * Definition for singly-linked list.
 * class ListNode {
 *     val: number
 *     next: ListNode | null
 *     constructor(val?: number, next?: ListNode | null) {
 *         this.val = (val===undefined ? 0 : val)
 *         this.next = (next===undefined ? null : next)
 *     }
 * }
 */

function mergeTwoLists(list1: ListNode | null, list2: ListNode | null): ListNode | null {
  if (!list1 && !list2) return null;

  if (!list1) return list2;
  if (!list2) return list1;

  const dummyHead = new ListNode(-101);
  let tail = dummyHead;

  let pointerOne: ListNode | null = list1;
  let pointerTwo: ListNode | null = list2;

  while (pointerOne && pointerTwo) {
    if (pointerOne.val <= pointerTwo.val) {
      tail.next = pointerOne;
      pointerOne = pointerOne.next;
    } else {
      tail.next = pointerTwo;
      pointerTwo = pointerTwo.next;
    }

    tail = tail.next;
  }

  if (pointerOne) {
    tail.next = pointerOne;
  } else {
    tail.next = pointerTwo;
  }

  return dummyHead.next;
}
