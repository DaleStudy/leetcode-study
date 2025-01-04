var mergeTwoLists = function (list1, list2) {
  // create a placeholder node and use it as a starting point
  let placeholder = { val: -1, next: null };
  let current = placeholder;

  // loop through the lists until one of them is fully traversed
  while (list1 !== null && list2 !== null) {
    if (list1.val <= list2.val) {
      // connect the element of list1 with the current node
      current.next = list1;
      // move list1 to its next node
      list1 = list1.next;
    } else {
      current.next = list2;
      list2 = list2.next;
    }
    // move the current pointer to the newly added node
    current = current.next;
  }
  current.next = list1 !== null ? list1 : list2;
  return placeholder.next;
};

// Time Complexity: O(n+m);
// Space Complexity: O(1)
