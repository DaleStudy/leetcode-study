/**
ListNode는 파라미터로 current value와 next value를 지닌다.
배열 메서드도 사용할 수 없다.

나는 원초적인 방법으로 해결해보았다.
result 배열에 모든 수를 다 넣고, sort()하는 것이다.
여기서 중요한 점은 '어떻게 배열 → ListNode로 변경하느냐'이다.
[1, 2, 3] 배열을 1 → 2 → 3 리스트 노드를 만들기 위해서는 컴퓨터 구조상 역방향인 3부터 가져와야한다.
이때 사용한 메서드는 'reduceRight()'다.
reduceRight() 메서드는 reduce() 작업순서의 역방향이다.

TC : O(nLogN) → sort()
SC : O(n)
 */
/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} list1
 * @param {ListNode} list2
 * @return {ListNode}
 */
function mergeTwoLists(list1, list2) {
  let result = [];
  let node1 = list1;
  let node2 = list2;

  while (node1 !== null) {
    result.push(node1.val);
    node1 = node1.next;
  }

  while (node2 !== null) {
    result.push(node2.val);
    node2 = node2.next;
  }

  return result
    .sort((a, b) => a - b)
    .reduceRight((next, val) => new ListNode(val, next), null);
}
