/*
주어진 단일 연결 리스트(singly linked list)는
각 노드가 하나의 값(val)과 다음 노드를 가리키는 포인터(next)를 가진다.

리스트의 첫 번째 노드는 head로 주어진다.

문제 목표:
  - 주어진 단일 연결 리스트의 노드 순서를 완전히 반대로 뒤집는다.
  - 뒤집힌 연결 리스트의 새로운 head를 반환한다.

중요한 조건:
  1) 단일 연결 리스트이므로 노드는 이전 노드를 직접 참조하지 않는다.
  2) 값의 순서를 바꾸는 것이 아니라, 노드 간 연결(next)의 방향을 변경해야 한다.
  3) 모든 노드는 그대로 사용하며 새 노드를 생성할 필요는 없다.

즉,
  원래 리스트:
    1 → 2 → 3 → 4 → 5 → null

  뒤집은 결과:
    5 → 4 → 3 → 2 → 1 → null

입력 형식:
  - head: 단일 연결 리스트의 첫 번째 노드 (ListNode)
  - ListNode는 다음 구조를 가진다:
      {
        val: 정수,
        next: ListNode | null
      }

제약 조건:
  - 노드의 개수는 0 이상 5000 이하
  - 각 노드의 값은 -5000 이상 5000 이하

출력 형식:
  - 뒤집힌 연결 리스트의 첫 번째 노드 (ListNode)

예시:

  Example 1
    입력: head = [1,2,3,4,5]
    출력: [5,4,3,2,1]

  Example 2
    입력: head = [1,2]
    출력: [2,1]

  Example 3
    입력: head = []
    출력: []
*/


function ListNode(val, next) {
  this.val = val === undefined ? 0 : val;
  this.next = next === undefined ? null : next;
}

/**
 * @param {ListNode} head
 * @return {ListNode}
 */
var reverseList = function(head) {
  let prev = null;
  let current = head;

  while (current !== null) {
    let next = current.next;
    current.next = prev;
    prev = current;
    current = next;
  }

  return prev;
};

// ===== 테스트 1 : [1,2,3,4,5]
const head1 =
  new ListNode(1,
    new ListNode(2,
      new ListNode(3,
        new ListNode(4,
          new ListNode(5)
        )
      )
    )
  );

// ===== 테스트 2 : [1,2]
const head2 = new ListNode(1, new ListNode(2));

// 결과 출력용
function printList(head) {
  const result = [];
  let cur = head;

  while (cur) {
    result.push(cur.val);
    cur = cur.next;
  }

  console.log(result);
}

// 실행
printList(reverseList(head1));
printList(reverseList(head2));


