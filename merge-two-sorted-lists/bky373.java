/**
 * TC: O(N)
 * SC: O(N)
 */
class Solution_21 {
    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
        if (list1 == null && list2 == null) {
            return null;
        }

        List<Integer> nums = new ArrayList<>();

        while (list1 != null) {
            nums.add(list1.val);
            list1 = list1.next;
        }
        while (list2 != null) {
            nums.add(list2.val);
            list2 = list2.next;
        }

        Object[] arr = nums.toArray();
        Arrays.sort(arr);

        ListNode head = new ListNode((int) arr[0]);
        ListNode curr = head;
        for (int i=1; i<arr.length; i++) {
            curr.next = new ListNode((int) arr[i]);
            curr = curr.next;
        }
        return head;
    }
}
