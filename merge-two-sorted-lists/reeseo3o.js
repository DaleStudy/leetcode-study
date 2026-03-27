/**
 * 1. Recursive approach
 * Time complexity: O(n + m)
 * Space complexity: O(n + m)
 */
// const mergeTwoLists = (list1, list2) => {
//     if (!list1) return list2;
//     if (!list2) return list1;
//
//     if (list1.val <= list2.val) {
//         list1.next = mergeTwoLists(list1.next, list2);
//         return list1;
//     } else {
//         list2.next = mergeTwoLists(list1, list2.next);
//         return list2;
//     }
// };

/**
 * 2. Iterative approach + Dummy Node
 * Time complexity: O(n + m)
 * Space complexity: O(1)
 */
const mergeTwoLists = (list1, list2) => {
    const dummy = new ListNode(-1);
    let current = dummy;

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

    current.next = list1 ?? list2;

    return dummy.next;
};
