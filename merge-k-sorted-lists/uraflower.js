/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode[]} lists
 * @return {ListNode}
 */
const mergeKLists = function (lists) {
    // 각 노드의 val 별 개수를 객체로 나타냄
    const counter = {};

    for (let list of lists) {
        let node = list;
        while (node) {
            counter[node.val] = (counter[node.val] || 0) + 1;
            node = node.next;
        }
    }

    // 위에서 만든 객체를 오름차순으로 순회하면서 node와 list를 생성
    let head = new ListNode();
    let current = head;
    const entries = Object.entries(counter).sort(([val1], [val2]) => Number(val1) - Number(val2)); // val 기준 오름차순 정렬

    for (let i = 0; i < entries.length; i++) {
        const [val, count] = entries[i];
        
        for (let j = 0; j < count; j++) {
            const node = new ListNode(Number(val));
            current.next = node;
            current = current.next;
        }
    }

    return head.next;
};

// 시간복잡도: O(n * log n) (sort에서 n * log n, 순회와 리스트 구성에서는 n)
// 공간복잡도: O(n)

// 최소힙을 통해 최적화를 할 수 있음
