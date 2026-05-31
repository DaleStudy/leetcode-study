/**
    연결 리스트를 활용하여, 하나의 리스트를 만드는 방식
    시간 복잡도 : O(N+M)
    공간 복잡도 : O(1)
 */
class Solution {
    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
        NodeList list=new NodeList();
        ListNode temp = null;
        while(list1 != null && list2 != null){
            if(list1.val >= list2.val){
                list2 = merge(list, list2);
            }else{
                list1 = merge(list, list1);
            }
        }
        while(list1 !=null){
            list1 = merge(list, list1);
        }
        while(list2 != null){
            list2 = merge(list, list2);
        }
        return list.head;
    }
    public class NodeList {
        ListNode head = null;
        ListNode tail = null;
        public NodeList(){
        }

        public void add(ListNode tempNode){
            if(head == null){
                head = tempNode;
                tail = head;
            }else{
                tail.next = tempNode;
                tail = tail.next;
            }
        }

    }

    public ListNode merge(NodeList list, ListNode target) {
        ListNode tempNode = null;
        tempNode = target;
        list.add(target);
        target = target.next;
        tempNode.next = null;
        return target;
    }
}
