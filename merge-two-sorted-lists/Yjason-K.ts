class ListNode {
    val: number
    next: ListNode | null
    constructor(val?: number, next?: ListNode | null) {
        this.val = (val===undefined ? 0 : val)
        this.next = (next===undefined ? null : next)
    }
}

/**
 * 두 개의 정렬된 연결 리스트를 병합하여 하나의 정렬된 연결 리스트를 반환하는 함수
 * @param {ListNode | null} list1 - 첫 번째 정렬된 연결 리스트
 * @param {ListNode | null} list2 - 두 번째 정렬된 연결 리스트
 * @returns {ListNode | null} - 병합된 정렬된 연결 리스트
 * 
 * 시간 복잡도: O(n + m)
 *  - n: list1의 노드 개수
 *  - m: list2의 노드 개수
 * 
 * 공간 복잡도: O(1)
 *  - 새로운 노드를 생성하지 않고 기존 노드의 포인터를 조정하여 병합하므로 추가 공간 사용 없음
 */

function mergeTwoLists(list1: ListNode | null, list2: ListNode | null): ListNode | null {
    // null 예외 처리
    if (!list1 || !list2) return list1 || list2;

    // 시작점을 위한 더미 헤드 노드 생성
    const start = new ListNode(-101);
    let current = start;

    // 두 리스트를 순차적으로 비교하며 병합
    while (list1 !== null && list2 !== null) {
        if (list1.val <= list2.val) {
            current.next = list1;
            list1 = list1.next;
        } else {
            current.next = list2;
            list2 = list2.next;
        }
        current = current.next;
    }

    // 남은 노드를 연결 (list1 또는 list2 중 하나는 null 상태)
    current.next = list1 !== null ? list1 : list2;

    // 더미 헤드의 다음 노드가 실제 병합된 리스트의 시작
    return start.next;
}
