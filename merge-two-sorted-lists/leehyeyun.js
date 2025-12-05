/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */

/*
  두 개의 정렬된 연결 리스트 list1과 list2의 head가 주어진다.

  두 리스트의 노드를 이어 붙여 하나의 정렬된 리스트를 만들고,
  그 병합된 연결 리스트의 head를 반환하는 함수.

  Example 1:
    Input:  list1 = [1,2,4], list2 = [1,3,4]
    Output: [1,1,2,3,4,4]

  Example 2:
    Input:  list1 = []
            list2 = []
    Output: []

  Example 3:
    Input:  list1 = []
            list2 = [0]
    Output: [0]

  Constraints:
    - 두 리스트의 노드 개수: 0 ~ 50
    - 노드 값 범위: -100 ~ 100
    - list1과 list2는 모두 오름차순(Non-decreasing order)으로 정렬됨
*/
/**
 * @param {ListNode} list1
 * @param {ListNode} list2
 * @return {ListNode}
 */

function ListNode(val, next) {
    this.val = (val===undefined ? 0 : val)
    this.next = (next===undefined ? null : next)
}

var mergeTwoLists = function(list1, list2) {
  //새로운 노드 생성 -> -1이라는 값은 쓰레기값
  let dummy = new ListNode(-1);
  let current = dummy;

  while (list1 !== null && list2 !== null) {
    //더 작은 값을 가진 노드를 현재 노드 뒤에 붙여줌
    if (list1.val < list2.val) {
      current.next = list1;
      list1 = list1.next; //다음 노드로 이동
    } else {
      current.next = list2;
      list2 = list2.next; //다음 노드로 이동
    }
    current = current.next; //새 노드를 붙인 뒤 이동
  }

  // 둘 중 하나가 남아 있으면 이어붙이기
  if (list1 !== null) current.next = list1;
  if (list2 !== null) current.next = list2;

  //dummy -1값은 제외하고 return하기 위해 dummy.next를 반환
  return dummy.next;
};

// Example 1
const list1 = new ListNode(1, new ListNode(2, new ListNode(4)));
const list2 = new ListNode(1, new ListNode(3, new ListNode(4)));

console.log("Example 1:");
console.log(JSON.stringify(mergeTwoLists(list1, list2), null, 2));

// Example 2
const list1_ex2 = null;
const list2_ex2 = null;

console.log("Example 2:");
console.log(JSON.stringify(mergeTwoLists(list1_ex2, list2_ex2), null, 2));

// Example 3
const list1_ex3 = null;
const list2_ex3 = new ListNode(0);

console.log("Example 3:");
console.log(JSON.stringify(mergeTwoLists(list1_ex3, list2_ex3), null, 2));


