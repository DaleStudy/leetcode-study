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

class ListNode {
  val: number
  next: ListNode | null
  constructor(val?: number, next?: ListNode | null) {
    this.val = (val===undefined ? 0 : val)
    this.next = (next===undefined ? null : next)
  }
}

function mergeTwoLists(list1: ListNode | null, list2: ListNode | null): ListNode | null {
  // list1과 list2의 val을 비교해나가면서 새로운 list 생성
  // 1. list1 없으면 list2 return
  if (!list1) return list2;
  // 2. list2 없으면 list1 return 
  if (!list2) return list1;

  const list = new ListNode(-101);

  let listNode = list;
  let listNode1: ListNode | null = list1;
  let listNode2: ListNode | null = list2;

  while (listNode1 && listNode2) {
    if (listNode1.val > listNode2.val) {
      listNode.next = new ListNode(listNode2.val, null);
      listNode2 = listNode2.next;
    }
    else {
      listNode.next = new ListNode(listNode1.val, null);
      listNode1 = listNode1.next;
    }
    listNode = listNode.next;
  }
  if (!listNode1) {
    listNode.next = listNode2;
  }
  else if (!listNode2) {
    listNode.next = listNode1;
  }

  return list.next;
};
