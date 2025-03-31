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
  public ListNode mergeKLists(ListNode[] lists) {
    List<ListNode> list = new LinkedList<>();
    for(ListNode l : lists) {
      list.add(l);
    }
    return divide(list);

  }
  public ListNode divide(List<ListNode> list) {
    //두개씩 나누기. 두개 안되면 그냥 리스트에 넣고 리턴
    int n = list.size();
    ListNode sum1;
    ListNode sum2;
    if(list.size() <= 2) {
      return merge(list);
    }

    int mid =  n / 2;
    List<ListNode> upper = new LinkedList<>();
    List<ListNode> last = new LinkedList<>();


    for(int i = 0; i < mid; i ++) {
      upper.add(list.get(i));

    }
    sum1 = divide(upper);


    for(int i = mid; i < n; i++) {
      last.add(list.get(i));
    }
    sum2 = divide(last);

    List<ListNode> m = new LinkedList<>();
    m.add(sum1);
    m.add(sum2);


    return merge(m);


  }
  public ListNode merge(List<ListNode> list) {
    //edge
    if(list.size()==0) return null;
    if(list.size() == 1) return list.get(0);

    ListNode n1 = list.get(0);
    ListNode n2 = list.get(1);
    // System.out.println(n1.val + " : " + n2.val);

    ListNode res = new ListNode(0);
    ListNode head = res;

    while(n1 != null && n2 != null) {
      if(n1.val < n2.val){
        res.next = n1;
        res = res.next;
        n1 = n1.next;
      } else {
        res.next = n2;
        res = res.next;
        n2 = n2.next;
      }

    }
    if(n1 == null) res.next = n2;
    if(n2 == null) res.next = n1;
    return head.next;



  }
}
