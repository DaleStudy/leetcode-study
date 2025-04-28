// Approach 2:
// ✅ Time Complexity: O(n)
// ✅ Space Complexity: O(1)

class ListNode {
  val: number;
  next: ListNode | null;
  constructor(val?: number, next?: ListNode | null) {
    this.val = val === undefined ? 0 : val;
    this.next = next === undefined ? null : next;
  }
}

function mergeTwoLists(
  list1: ListNode | null,
  list2: ListNode | null
): ListNode | null {
  let dummy = new ListNode(0);
  let current = dummy;

  while (list1 && list2) {
    if (list1.val <= list2.val) {
      current.next = list1;
      list1 = list1.next;
    } else {
      current.next = list2;
      list2 = list2.next;
    }
    current = current.next;
  }

  current.next = list1 || list2; // Attach whatever is left

  return dummy.next;
}


// Approach 1: works, but not efficient for big inputs
// Time Complexity: O(n log n)
// Space Complexity: O(n)

// function mergeTwoLists(
//   list1: ListNode | null,
//   list2: ListNode | null
// ): ListNode | null {
//   let stack: number[] = [];

//   const dfs = (node: ListNode | null) => {
//     if (!node) {
//       return;
//     }

//     stack.push(node.val);

//     return dfs(node.next);
//   };

//   dfs(list1);
//   dfs(list2);

//   stack.sort((a, b) => a - b);

//   if (stack.length === 0) {
//     return null;
//   }

//   let merged = new ListNode();
//   let dummy = merged;

//   for (let i = 0; i < stack.length; i++) {
//     dummy.val = stack[i];

//     if (i !== stack.length - 1) {
//       dummy.next = new ListNode();
//       dummy = dummy.next;
//     } else {
//       dummy.next = null;
//     }
//   }

//   return merged;
// }
