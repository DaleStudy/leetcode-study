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
/**
 * head는 연결 리스트의 헤드다.
 * 특정 노드가 리스트 내의 다른 노드와 next 포인트를 통해 연결되어 있을 때 이 리스트에는 사이클이 있다고 할 수 있다.
 * pos는 next 포인터와 연결된 노드의 인덱스를 나타내는데 쓰이며 pos는 파라미터로 주어지지 않는다.
 * 주어진 리스트에 사이클이 있다면 true를 그렇지 않다면 false를 반환하세요.
 * */
public class Solution {

    // 시간복잡도: O(n), 공간복잡도: O(1)
    public boolean hasCycle(ListNode head) {
        if (head == null) {
            return false;
        }

        ListNode next = head;
        ListNode furtherNext = head;

        while (furtherNext != null && furtherNext.next != null) {
            next = next.next;
            furtherNext = furtherNext.next.next;
            if (next == furtherNext) {
                return true;
            }
        }

        return false;
    }

    // head 없을 때까지 계속 탐색 반복 : 시간복잡도, 공간복잡도 O(n)
    // public boolean hasCycle(ListNode head) {

    //     Set<ListNode> nodeSet = new HashSet<>();

    //     while (head != null) {
    //         if (nodeSet.contains(head)) {
    //             return true;
    //         }
    //         nodeSet.add(head);
    //         head = head.next;
    //     }

    //     return false;

    // }
}

