
class ListNode {
    val: number
    next: ListNode | null
    constructor(val?: number, next?: ListNode | null) {
        this.val = (val===undefined ? 0 : val)
        this.next = (next===undefined ? null : next)
    }
}
 

function mergeTwoLists(list1: ListNode | null, list2: ListNode | null): ListNode | null {
  let mergedList = new ListNode(0, null);
  const result = mergedList;

  while(list1 && list2) {
      if(list1.val < list2.val) {
          mergedList.next = list1;
          list1 = list1.next;
      } else {
          mergedList.next = list2;
          list2 = list2.next;
      }
      mergedList = mergedList.next;
  }

  mergedList.next = list1 ?? list2;
  
  return result.next;
};
