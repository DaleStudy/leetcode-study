
/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @return {ListNode}
 */
var reverseList = function(head) {
    if (head === null) {
      return null;
    }
  
    if (head.next === null) {
      return head;
    }
  
    const stack = [];
  
    let nextNode = head;
    
    while (nextNode) {
      stack.push(nextNode);
  
      nextNode = nextNode.next;
    }
  
    for (let i=stack.length - 1; i>=0; i--) {
      if (i === 0) {
          stack[i].next = null;
      } else {
          stack[i].next = stack[i - 1];
      }
    }
  
  return stack[stack.length - 1];
};

// 시간복잡도 O(2n)


