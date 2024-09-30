/**
 * 풀이
 * - 주어진 두 링크드리스트의 각 node를 비교하며 반환할 새 링크드리스트에 추가해줍니다
 * 
 * Big O
 * - N: 주어진 두 링크드리스트 list1, list2의 노드 개수의 총합
 * 
 * - Time complexity: O(N)
 * - Space complexity: O(1)
 *   - 반환하는 링크드리스트를 복잡도에 포함시키지 않을 시, 공간복잡도는 N에 상관 없이 일정합니다
 */

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {
        ListNode* head = new ListNode();
        ListNode* node = head;

        ListNode* p = list1;
        ListNode* q = list2;

        while (p != nullptr && q != nullptr) {
            if (p->val < q->val) {
                node->next = p;
                p = p->next;
            } else {
                node->next = q;
                q = q->next;
            }
            node = node->next;
        }

        while (p != nullptr) {
            node->next = p;
            p = p->next;
            node = node->next;
        }

        while (q != nullptr) {
            node->next = q;
            q = q->next;
            node = node->next;
        }

        return head->next;
    }
};