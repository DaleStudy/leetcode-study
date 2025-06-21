/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */

// 첫 번째 풀이
// 시간복잡도: O(n)
// 공간복잡도: O(n)
/**
 * @param {ListNode} head
 * @param {number} n
 * @return {ListNode}
 */
const removeNthFromEnd = function (head, n) {
    function dfs(node) {
        // 마지막 노드이면 1 반환
        if (!node.next) {
            return 1;
        }

        const nth = dfs(node.next);
        if (nth === n) {
            node.next = node.next.next ?? null;
        }

        return nth + 1;
    }

    if (dfs(head) === n) {
        return head.next;
    }

    return head;
};

// 두 번째 풀이
// 시간복잡도: O(n)
// 공간복잡도: O(1)
const removeNthFromEnd = function (head, n) {
    const temp = new ListNode(0, head);
    let tail = temp; 
    let prev = temp; // 뒤에서 n번째 노드
    
    for (let i = 0; i < n; i++) {
        tail = tail.next;
    }

    while (tail.next) {
        tail = tail.next;
        prev = prev.next;
    }
    
    prev.next = prev.next.next;

    return temp.next;
};
