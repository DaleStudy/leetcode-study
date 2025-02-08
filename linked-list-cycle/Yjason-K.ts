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

/**
 * 연결 리스트인가 순환하는지 여부 확인
 * @param {ListNode} head - ListNode 
 * @returns {boolean} - 순환 여부
 * 
 * 시간 복잡도: O(n)
 * 
 * 공간 복잡도: O(n)
 *  -  노드의 개수만큼 Set에 저장
 */
function hasCycle(head: ListNode | null): boolean {
    const set = new Set();

    while (head) {
        if (set.has(head)) {
            return true;
        }

        set.add(head);
        head = head.next;
    }

    return false;
}

