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
    let prev = null; // 1 | 
    let current = head; // [null, 2] | []
    let next = null // 2 | 3

    // prev = null
    // current = 1
    // next =2 

    // prev = 1
    // current = 2
    // next = 3
    
    // prev = 2
    // current = 3
    // next = 4

    // prev = 3
    // current = 4
    // next = 5

    // prev = 4
    // current = 5
    // next = null

    while(current != null){
        next = current.next;
        current.next = prev
        prev = current;
        current = next;
    }   

    head = prev
    return head
};

