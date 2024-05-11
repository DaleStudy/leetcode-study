var mergeTwoLists = function(list1, list2) {
    // check if either of the input lists is null.
    if (!list1) return list2;
    if (!list2) return list1;

    // create a dummy node.
    let dummy = new ListNode();
    let current = dummy;

    // compare the values pointed to by list1 and list2.
    while (list1 && list2) {
        // append the smaller value to the merged list pointed to by current.
        if (list1.val < list2.val) {
            current.next = list1;
            list1 = list1.next;
        } else {
            current.next = list2;
            list2 = list2.next;
        }
        current = current.next;
    }

    // ensure any remaining nodes are appended.
    current.next = list1 || list2;

    return dummy.next;
};

// Time complexity : O(n+m)
// Space complexity : O(1)
