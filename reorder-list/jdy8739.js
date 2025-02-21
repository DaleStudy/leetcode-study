/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @return {void} Do not return anything, modify head in-place instead.
 */
var reorderList = function (head) {
    if (!head) {
        return null;
    }

    const stack = [];

    let node = head;

    while (node) {
        stack.push(node);
        node = node.next;
    }

    const length = stack.length;

    node = head;
    let count = 0;

    while (count < length) {
        if (count % 2 === 0) {
            const top = stack.pop();

            top.next = node.next;

            node.next = top;
        }

        if (count === length - 1) {
            node.next = null;
        } else {
            node = node.next;
        }

        count++;
    }


    return head;
};

// 시간복잡도 O(n) -> while문이 링크드리스트의 길이만큼 순회를하기때문에 링크드리스트의 길이만큼 시간이 걸림
// 공간복잡도 O(n) -> 스택에 모든 노드를 저장하기 때문에 링크드리스트의 길이만큼 공간이 필요
