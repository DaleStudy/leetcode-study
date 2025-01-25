/**
 * @param {ListNode} head
 * @return {ListNode}
 * 
 * 접근
 * ListNode 타입에 대해서 공부하고, 링크드 리스트 개념을 접목해서 문제를 풀이
 * 
 * complexity
 * time: O(n)
 * space: O(1)
 */
var reverseList = function(head) {
  let newList = null
  let curNode = null
  
  while(head){
      curNode = head.next
      head.next = newList
      newList = head
      head = curNode 
  }

  return newList
};

