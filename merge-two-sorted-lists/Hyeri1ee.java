import java.util.*;



 
class Solution {
    
   
    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
        ListNode merged = new ListNode();//머지 된 노드 모음
        ListNode temp = merged;
        while(list1 != null && list2 != null){

            ListNode newNode = new ListNode();//새로운 노드
            if (list1.val > list2.val){
                //list2
                newNode.val = list2.val;
                list2 =list2.next;//다음 가리키도록\
               // merged.next
            }else{
                newNode.val =list1.val;
                list1=list1.next;//다음 가리키도록
            }

            merged.next = newNode;
            merged =merged.next;

        }        

        if (list1==null)
            merged.next= list2;
        else if (list2 == null)
            merged.next=list1;

        return temp.next;
    }
}
