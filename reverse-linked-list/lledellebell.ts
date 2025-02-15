/**
 * @problem
 * 단일 연결 리스트를 뒤집는 알고리즘을 함수형 프로그래밍 스타일로 구현합니다.
 * 예: 1 -> 2 -> 3 -> 4 -> 5 -> => 5 -> 4 -> 3 -> 2 -> 1
 * 
 * @constraints
 * - 노드의 개수는 0 이상일 수 있습니다.
 * - 각 노드의 값은 정수입니다.
 * - 입력 리스트는 단일 연결 리스트입니다.
 *
 * @example
 * - Input: head = [1, 2, 3, 4, 5]
 * - Output: [5, 4, 3, 2, 1]
 *
 * @description
 * 재귀를 사용하여 연결 리스트를 뒤집습니다. 
 * 함수형 프로그래밍 스타일에서는 상태를 변경하지 않고, 각 호출에서 새로운 리스트를 반환합니다.
 *
 * @complexity
 * - 시간 복잡도: O(n)
 *   리스트의 모든 노드를 한 번씩 방문합니다.
 * - 공간 복잡도: O(n)
 *   재귀 호출 스택을 사용합니다.
 */
class ListNode {
    val: number;
    next: ListNode | null;

    /**
     * @constructor
     * @param val - 노드의 값
     * @param next - 다음 노드에 대한 참조
     */
    constructor(val?: number, next?: ListNode | null) {
        this.val = val ?? 0; // 값이 없으면 기본값 0
        this.next = next ?? null; // 다음 노드가 없으면
    }
}

/**
 * 단일 연결 리스트를 뒤집는 함수 (재귀적, 함수형 스타일)
 * @param head - 연결 리스트의 시작 노드
 * @param prev - 이전 노드 (초기값은)
 * @returns 뒤집힌 연결 리스트의 시작 노드
 */
function reverseList(
    head: ListNode | null,
    prev: ListNode | null = null
): ListNode | null {
    // 기본 조건: 리스트가 비어 있거나 마지막 노드에 도달한 경우
    if (head === null) {
        return prev;
    }

    // 다음 노드 저장
    const next = head.next;

    // 현재 노드의 방향을 이전 노드로 설정
    head.next = prev;

    // 재귀 호출로 다음 노드 처리
    return reverseList(next, head);
}

// 연결 리스트 생성
const node1 = new ListNode(1);
const node2 = new ListNode(2);
const node3 = new ListNode(3);
const node4 = new ListNode(4);
const node5 = new ListNode(5);

node1.next = node2;
node2.next = node3;
node3.next = node4;
node4.next = node5;

const reversedHead = reverseList(node1);

// 결과
let current = reversedHead;
while (current !== null) {
    console.log(current.val); // 5, 4, 3, 2, 1
    current = current.next;
}
