function ListNode(val, next) {
  this.val = val === undefined ? 0 : val;
  this.next = next === undefined ? null : next;
}

/**
 * @param {ListNode} list1
 * @param {ListNode} list2
 * @return {ListNode}
 */
var mergeTwoLists = function (list1, list2) {
  if (!list1 && !list2) {
    return null;
  }

  if (!list1 || !list2) {
    return [list1, list2].find(Boolean);
  }

  // firstPointer is a head of list who has the smallest value of node
  let [firstPointer, secondPointer] =
    list1.val < list2.val ? [list1, list2] : [list2, list1];
  const mergedList = firstPointer;

  if (firstPointer.next === null) {
    firstPointer.next = secondPointer;
    return mergedList;
  }

  while (secondPointer !== null) {
    let nextFirstPointer = firstPointer.next;
    const nextSecondPointer = secondPointer.next;

    while (
      firstPointer.next !== null &&
      firstPointer.next.val < secondPointer?.val
    ) {
      firstPointer = firstPointer.next;
      nextFirstPointer = firstPointer.next;
    }

    firstPointer.next = secondPointer;
    firstPointer.next.next = nextFirstPointer;

    secondPointer = nextSecondPointer;
    firstPointer = firstPointer.next;
  }

  return mergedList;
};
