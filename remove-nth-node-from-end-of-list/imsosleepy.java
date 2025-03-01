 // 노드 전체를 한번만 탐색하게 만들었음 따라서 O(N)
 // 투포인터 방식으로 하나를 N+1 위치로 보내서 N번째 노드를 제거한 후 oneStep과 연결한다.
 // oneStep은 삭제할 노드 바로 직전 노드 
 // 사이즈가 1일 때를 범용적으로 처리하기 위해 머리를 굴렸음...
class Solution {
    public ListNode removeNthFromEnd(ListNode head, int n) {
        ListNode defaultNode = new ListNode(0); 
        defaultNode.next = head;
        ListNode twoStep = defaultNode;
        ListNode oneStep = defaultNode;

        for (int i = 0; i <= n; i++) {
            twoStep = twoStep.next;
        }

        while (twoStep != null) {
            twoStep = twoStep.next;
            oneStep = oneStep.next;
        }

        oneStep.next = oneStep.next.next;
        
        return defaultNode.next;
    }
}
