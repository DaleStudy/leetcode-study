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
    const nodes = {};
    let current = head;
    let n = 0; // 인덱스 역할
    
    // 리스트를 순회하면서 각 노드를 객체에 저장
    while (current) {
        nodes[n] = current;
        current = current.next;
        nodes[n].next = null;   // 여기서 모든 노드의 next를 null로 변경
                                // 이렇게 안 하면 next 바꾸기 한 다음에 맨 마지막 노드의 next만 null로 바꿔야 함
        n++
    }

    // 저장한 노드를 i, n-i, ... 순서로 접근하면서 next 바꾸기
    for (let i = 0; i < Math.floor(n / 2); i++) {
        nodes[i].next = nodes[n - i - 1];

        // n-i-1 === i+1 인 경우, node.next = node 처럼 셀프 순환이 될 수 있음
        if (n - i - 1 !== i + 1) {
            nodes[n - i - 1].next = nodes[i + 1];
        }
    }
};

// 시간복잡도: O(n)
// 공간복잡도: O(n)
