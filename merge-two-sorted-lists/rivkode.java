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
 /*
 1. 문제 이해
 두개의 정렬된 리스트를 머지한다
 이때 이미 정렬된 리스트를 합치는 것이므로 2개의 head를 비교해서 작거나 같은 것을 next로 붙이면 된다

 2. 알고리즘
 while 사용, 재귀

 3. 예외 케이스

 둘중에 하나의 리스트가 먼저 null 이 되버리면 나머지 리스트도 붙여줘야 하므로 while 문이 끝난 뒤에 붙여줘야 한다.
 
 4. 구현
 각 head를 비교해서 더 작은 것을 head 로 두고 작은것의 next와 다른 리스트의 head 를 다시 비교한다
 만약 같다면 둘중 하나를 선택한다
아니다
이렇게 순서가 되어야 하지 않을까
#0 리스트1과 리스트2가 Null이 아닌지 체크한다 Null 이면 head 반환.
#1 두개의 비교할 노드를 초기화 한다
#2 두개의 값을 비교한다
#3 작은 값을 이전 Head의 Next로 정한다
#4 작은 값의 next를 다시 비교할 노드로 세팅한다
#5 2번으로 다시 돌아가서 반복한다

즉 비교할 노드를 초기화 하고
비교해서 next로 넣고
다시 초기화 해서 비교한다

 예를 들어
 1 - 2 - 3
 3 - 4 - 5
 일 경우
 1이 작으므로 1을 head 로 두고
 next를 구하기 위해 1의 Next와 3을 비교한다
 1의 Next가 2이므로 1의 next는 2가 된다
 2의 Next와 3을 다시 비교한다

답지를 보니 재귀로도 풀 수 있고 내가 한 방식으로도 풀 수 있네.

가장 앞에 dummy를 두어서 head를 세팅할 수 있다는 생각을 해야겠다.
 */
class Solution {
    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
        ListNode dummy = new ListNode(-1);
        ListNode node = dummy;

        while (list1 != null && list2 != null) {
            // 각 리스트의 값을 비교
            if (list1.val < list2.val) {
                node.next = list1;
                list1 = list1.next;
            } else {
                node.next = list2;
                list2 = list2.next;
            }

            // Node 의 커서를 다음으로 이동
            node = node.next;
        }

        // 나머지 부분을 현재 Node 의 next를 붙여주기 위함
        node.next = l1 != null ? l1 : l2;
        
        return dummy.next;
    }
}
