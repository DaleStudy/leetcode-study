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
전달받은 링크드 리스트를 역방향으로 된 리스트 헤드 반환

2. 알고리즘
스택, 역방향이므로 가장 아래까지 내려가서 다시 리스트를 만들어준다.
답지 참고: 스택으로 해도 되지만 방향만 바꾸어도 된다.

3. 예외
헤드가 없을 경우

4. 구현

헤드 널 확인
헤드를 스택에 넣는다
for loop를 돌면서 next 가 null 일때까지 스택에 넣는다

다시 스택의 가장 마지막부터 링크드 리스트를 만든다.
만든 리스트의 헤드를 반환한다.

cur, prev 노드를 각 순서대로 지정하여 포인터 방향을 바꾸어준다.
a. 다음 노드를 임시 저장한다
b. 현재 노드의 next 를 이전 노드로 설정한다. (방향 변환)
[변환이 끝났으므로 다음 노드를 위한 초기화를 해야함]
c. prev 를 현재의 노드인 cur 로 초기화 한다.
d. cur 를 실제 다음 노드로 초기화 한다. 즉 한칸 뒤로 이동하게 되는 효과가 있다.

*/
import java.util.*;

class Solution {
    public ListNode reverseList(ListNode head) {
        ListNode prev = null;
        ListNode cur = head;

        // cur 이 null 일떄까지 반복루프
        while (cur != null) {
            // 다음 노드를 현재의 이전 노드로 방향을 바꾸면 초기화되므로 다음 노드를 임시 노드에 할당
            ListNode tempNext = cur.next;
            // 핵심, 현재의 next 를 prev 로 함으로써 방향 변환
            cur.next = prev;
            // 현재 노드를 prev 에 할당, prev 초기화
            prev = cur;
            // 다음 노드를 cur 에 할당, cur 초기화
            cur = tempNext;
        }

        return prev;
    }
}

