/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */

/**
 * @param {ListNode} head
 * @return {boolean}
 */
var hasCycle = function (head) {

    const visited = new Set();
    let result = false;

    while (head) {

        let next = head.next;

        if (next == null) {
            result = false;
            break;
        }

        let isExist = findElementInDp(head);

        if (!isExist) {
            visited.add(head);
            head = next;
        } else {
            result = true;
            break;
        }
    }

    return result;

    function findElementInDp(head) {
        if (visited.has(head)) {
            return true;
        } else {
            return false;
        }
    }
};
