class ListNode {
  val: number;
  next: ListNode | null;
  constructor(val?: number, next?: ListNode | null) {
    this.val = val === undefined ? 0 : val;
    this.next = next === undefined ? null : next;
  }
}

// TC: O(n)
// SC: O(1)
function removeNthFromEnd(head: ListNode | null, n: number): ListNode | null {
  let dummy = new ListNode();
  dummy.next = head;
  let fast: ListNode | null = dummy;
  let slow: ListNode | null = dummy;

  for (let i = 0; i < n + 1; i++) {
    if (fast) {
      fast = fast.next;
    }
  }

  while (fast) {
    fast = fast.next;
    slow = slow!.next;
  }

  if (slow && slow.next) {
    slow.next = slow.next.next;
  }

  return dummy.next;
}


// TC: O(n)
// SC: O(n)
// function removeNthFromEnd(head: ListNode | null, n: number): ListNode | null {
//   let dummy = head;
//   const nodes: (ListNode | null)[] = [];

//   while (dummy) {
//     nodes.push(dummy);
//     dummy = dummy.next;
//   }

//   // first node: nodes.length === n
//   // last node: n === 1

//   if (nodes.length === n) {
//     head = head!.next;
//   } else if (nodes.length > 1 && n === 1) {
//     nodes[nodes.length - 2]!.next = null;
//   } else {
//     nodes[nodes.length - n - 1]!.next = nodes[nodes.length - n + 1];
//   }

//   return head;
// }
