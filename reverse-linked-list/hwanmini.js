// 시간복잡도: O(n)
// 공간복잡도: O(1)

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
    let curNode = head
    let preNode = null

    while (curNode) {
        const nextNode = curNode.next
        curNode.next = preNode
        preNode = curNode
        curNode = nextNode
    }


    return preNode
};
