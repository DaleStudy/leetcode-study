// 시간복잡도 O(N + M)
class Solution {

    public ListNode root = null;
    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {

        while(list1 != null || list2 != null) {
            int v1 = 9999;
            int v2 = 9999;
            
            if(list1 != null) {
                v1 = list1.val;
            }

            if(list2 != null) {
                v2 = list2.val;
            }

            if(v1 < v2) {
                addNode(v1);
                list1 = list1.next;    
            } else {
                addNode(v2);
                list2 = list2.next;
            }      
        }

        return root;
    }

    public void addNode (int val) {
        if(root == null) {
            root = new ListNode(val);
            return;
        }

        ListNode now = root;
        while(now.next != null) {
            now = now.next;
        }

        now.next = new ListNode(val);
    }
}
