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
 * linked list 를 뒤집는 함수.
 *
 * @param {ListNode | null} head - linked list 의 시작 노드
 * @returns {ListNode | null} 뒤집힌 단일 연결 리스트의 시작 노드
 *
 * - 시간 복잡도(Time Complexity): O(n)  
 *   - llinked list 길이 만큼 순회
 *
 * - 공간 복잡도(Space Complexity): O(1)
 */
function reverseList(head: ListNode | null): ListNode | null {
    let prev: ListNode | null = null;
    let curr: ListNode | null = head;
  
    while (curr !== null) {
      const next: ListNode | null = curr.next; // 다음 노드를 잠시 저장
      curr.next = prev; // 현재 노드의 next를 이전 노드를 가리키도록 변경
      prev = curr;      // prev를 현재 노드로 업데이트
      curr = next;      // curr를 다음 노드로 이동
    }
  
    return prev; // prev가 뒤집힌 연결 리스트의 시작 노드가 됩니다.
};

