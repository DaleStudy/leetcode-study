/*
1. 문제 이해
링크드 리스트가 루프인지 아닌지 판단하는 문제
만약 동일한 노드를 방문한다면 그것은 링크드 리스트 루프임
만약 노드의 next가 null이면 이 리스트는 루프가 아닌 링크드 리스트

2. 예외

0개와 한개일때 이 부분은 루프가 아니므로 false

3. 알고리즘
Set을 사용해서 순차적으로 노드를 넣고 만약 동일한 노드가 있다면 그것은 루프를 돌았다는 의미로 false 반환

4. 구현
초기화
set 자료구조

while (isnextnull)

1. 현재 노드의 next가 null인지 판단
2. null일 경우 res를 false로 초기화 및 루프 탈출
3. null이 아니면 set에 자료구조 체크
3-1. set에 없으면 넣고 다음 루프 진행
3-2. set에 있으면 res를 false로 초기화 및 루프 탈출

*/

/**
 * Definition for singly-linked list.
 * class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */

import java.util.*;

public class Solution {
    public boolean hasCycle(ListNode head) {
        Set<ListNode> set = new HashSet<>();
        if (head == null) {
            return false;
        }
        
        ListNode curNode = head.next;
        boolean isNextNull = false;
        boolean res = true;

        // head node check
        if (curNode == null) {
            return false;
        }

        ListNode next;

        while (true) {
            next = curNode.next;
            if (next == null) {
                res = false;
                break;
            }
            if (set.contains(next)) {
                res = true;
                break;
            }
            set.add(next);
            // node 초기화
            curNode = curNode.next;
        }

        return res;
    }
}

