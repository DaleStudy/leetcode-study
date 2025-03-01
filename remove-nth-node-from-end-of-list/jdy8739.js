/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @param {number} n
 * @return {ListNode}
 */
var removeNthFromEnd = function (head, n) {
    if (!head) {
        return null;
    }

    let node = head;

    const list = [];

    while (node) {
        list.push(node);
        node = node.next;
    }

    const targetIndex = list.length - n - 1;

    if (targetIndex === -1 && list.length === 1) {
        return null;
    }

    if (targetIndex === -1) {
        return head.next;
    }
    
    if (list[targetIndex]) {
        list[targetIndex].next = list[targetIndex]?.next?.next || null;
    }

    return head;
};

// 시간복잡도 O(n) - 노드를 한번 순회하여 리스트에 저장
// 공간복잡도 O(n) - 순회 이후에 제거할 노드의 바로 앞 노드레 접근하기 위하여 모든 노드를 배열에 저장
