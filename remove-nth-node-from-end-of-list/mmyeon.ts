class ListNode {
  val: number;
  next: ListNode | null;
  constructor(val?: number, next?: ListNode | null) {
    this.val = val === undefined ? 0 : val;
    this.next = next === undefined ? null : next;
  }
}

/**
 *@link https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/
 *
 * 접근 방법 :
 *  - 리스트 순회해서 리스트 사이즈 알아낸 뒤, 앞에서부터 몇 번째 노드를 제거해야하는지 알아내기
 *  - 리스트 다시 순회해서 해당 인덱스의 노드 제거하기
 *
 * 시간복잡도 : O(n)
 *  - n = 리스트 길이
 *  - 1회 순회 -> 리스트 길이 알아내기, 추가로 1회 순회해서 노드 제거
 *
 * 공간복잡도 : O(1)
 *  - 고정된 변수만 사용
 */
function removeNthFromEnd(head: ListNode | null, n: number): ListNode | null {
  let listSize = 0;
  let current = head;

  // 리스트 길이 구하기
  while (current) {
    listSize++;
    current = current.next;
  }

  // 제거할 노드의 인덱스
  const targetIndex = listSize - n;
  let currentIndex = 0;

  current = head;

  if (targetIndex === 0) return head ? head.next : null;

  while (current) {
    if (currentIndex === targetIndex - 1 && current.next) {
      current.next = current.next.next;
      break;
    }
    currentIndex++;
    current = current.next;
  }

  return head;
}

/**
 *
 * 접근 방법 : two pointer 사용
 *  - 첫 번째 노드가 제거되는 경우가 존재하니까, dummy 노드 만들어서 헤드 노드로 설정
 *  - fast 포인터의 초기 위치를 n+1로 설정하기
 *  - 이후에는 slow 포인터와 fast 포인터 모두 1개씩 다음 노드로 순회
 *  - fast 포인터가 끝에 도달하면, slow 포인터는 삭제할 노드 이전 노드에 도달
 *
 * 시간복잡도 : O(n)
 *  - n = 리스트 길이
 *  - 1회 순회로 삭제할 노드 알아내기
 *
 * 공간복잡도 : O(1)
 *  - 고정된 변수만 사용
 */
function removeNthFromEnd(head: ListNode | null, n: number): ListNode | null {
  if (head === null) return null;

  const dummy = new ListNode();
  dummy.next = head;

  let slow: ListNode | null = dummy,
    fast: ListNode | null = dummy;

  // fast 포인트 위치 n+1으로 초기 세팅
  for (let i = 0; i <= n; i++) {
    fast = fast.next!;
  }

  while (fast !== null) {
    slow = slow.next!;
    fast = fast.next;
  }

  // 다음 노드 삭제
  slow.next = slow.next!.next;

  return dummy.next;
}
