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
    let prev = null; 
    let current = head; 
    let next = null 

    while(current != null){
        next = current.next;
        current.next = prev
        prev = current;
        current = next;
    }   

    head = prev
    return head
};

