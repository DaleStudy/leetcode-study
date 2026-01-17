
class Solution {
    public ListNode mergeKLists(ListNode[] lists) {
            ListNode list= new ListNode(0); // head
            ListNode curr=list;
            PriorityQueue<ListNode> pq=new PriorityQueue<ListNode>((l1, l2)->{
                return l1.val - l2.val;
            });
            for(int i=0; i<lists.length;i++){
                if(lists[i]!=null){
                    pq.offer(lists[i]);
                }
            }
            while(!pq.isEmpty()){
                ListNode temp = pq.poll();
                curr.next=new ListNode(temp.val);
                curr=curr.next;
                temp=temp.next;
                if(temp!=null){
                    pq.offer(temp);
                }

            }
            return list.next;
                
        
    }
}
