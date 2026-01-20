/*

*/
class Solution {
    public void reorderList(ListNode head) {
        List<ListNode> list = new ArrayList<>();

        while(head != null) {
            list.add(head);
            head= head.next;
        }

        int i = 0;
        int j = list.size() -1;
        while(i < j) {
            ListNode left = list.get(i);
            ListNode right = list.get(j);

            left.next = right;
            i++;

            if (i == j) {
                right.next = null;
                break;
            }

            right.next = list.get(i);
            j--;
        }

        list.get(i).next = null;
    }
}
