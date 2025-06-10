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

function mergeKLists(lists: Array<ListNode | null>): ListNode | null {
    const tempArray: Array<ListNode> = []
    lists.forEach((node) => {
        while (node) {
            tempArray.push(node)
            node = node.next
        }
    })
    tempArray.sort((node1, node2) => node1.val - node2.val)
    let result = tempArray[0] ?? null
    tempArray.forEach((node, index, arr) => {
        node.next = arr[index + 1] ?? null
    })
    return result
};
