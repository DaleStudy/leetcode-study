/* [5th/week04] 21. Merge Two Sorted Lists

1. 문제 요약
링크: https://leetcode.com/problems/merge-two-sorted-lists/description/
두 개의 정렬된 리스트를 오름차순으로 병합한 리스트를 반환

2. 문제 풀이
풀이1: 두 리스트의 head 비교해서 더 작은 값 선택 -> 한쪽이 null되면 재귀를 통해 이어붙여서 마무리
성공/실패: 시간 복잡도는 O(m+n), 공간 복잡도는 O(m+n) 
=> Time: 0 ms (100%), Space: 43 MB (8.18%)

class Solution {
    public ListNode mergeTwoLists(ListNode l1, ListNode l2) {
        if (l1 == null || l2 == null)
            return l1 != null ? l1 : l2;
        if (l1.val < l2.val) {
            l1.next = mergeTwoLists(l1.next, l2);
            return l1;
        } else {
            l2.next = mergeTwoLists(l1, l2.next);
            return l2;
        }
    }
}

풀이2: 두 리스트의 head 비교해서 더 작은 값 선택해서 node.next에 연결 -> 한쪽이 null되면 dummy.next 반환
성공/실패: 시간 복잡도는 O(m+n), 공간 복잡도는 O(1) 
=> Time: 0 ms (100%), Space: 43.2 MB (8.18%)

class Solution {
    public ListNode mergeTwoLists(ListNode l1, ListNode l2) {
        ListNode dummy = new ListNode(-1); 
        ListNode node = dummy; 

        while (l1 != null && l2 != null) {
            if (l1.val < l2.val) {
                node.next = l1;
                l1 = l1.next;
            } else {
                node.next = l2;
                l2 = l2.next;
            }
            node = node.next;
        }

        node.next = l1 != null ? l1 : l2;
        return dummy.next;
    }
}

*/

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
    public ListNode mergeTwoLists(ListNode l1, ListNode l2) {
        ListNode dummy = new ListNode(-1); 
        ListNode node = dummy;

        while (l1 != null && l2 != null) {
            if (l1.val < l2.val) {
                node.next = l1;
                l1 = l1.next;
            } else {
                node.next = l2;
                l2 = l2.next;
            }
            node = node.next;
        }

        node.next = l1 != null ? l1 : l2;
        return dummy.next;
    }
}
