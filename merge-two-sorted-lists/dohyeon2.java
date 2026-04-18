/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    // TC : O(n)
    // SC : O(n)
    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
        // Initialize anonymous head for result
        ListNode result = new ListNode(0);
        // Initialize cursor to track list
        ListNode cursor = result;
     
        // If any list remains
        while(list1 != null || list2 != null){
            // Choose the smaller node
            if(list2 == null 
            || (list1 != null && list1.val <= list2.val)){
                cursor.next = list1;
                list1 = list1.next;
            }else{
                cursor.next = list2;
                list2 = list2.next;
            }
            //Set the cursor to the next
            cursor = cursor.next;
        }

        // Skip dummy head and return the actual merged list
        return result.next;
    }
}
