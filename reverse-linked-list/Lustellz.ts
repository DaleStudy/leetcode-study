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

// Runtime: 0ms
// Memory: 58.86MB

function reverseList(head: ListNode | null): ListNode | null {
    let previousNode: ListNode | null = null;
    let currentNode: ListNode | null = head;
    while(currentNode){
        const nextNode: ListNode | null = currentNode.next; // mark nextNode's value of current node temporary
        currentNode.next = previousNode; // set next node of current as previous node
        previousNode = currentNode; // set previous node as current node
        currentNode = nextNode; // move to nextNode
    }
    return previousNode // currentNode would be null if it reaches the end of the node list
};
