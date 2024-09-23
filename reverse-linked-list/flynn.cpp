/**
 * 풀이
 * - 생략, 주석 참고
 * 
 * Big O
 * - N: 주어진 링크드 리스트 `head`의 길이
 * 
 * - Time complexity: O(N)
 * - Space complexity: O(1)
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
    ListNode* reverseList(ListNode* head) {
        if (head == nullptr) return head;
        // example: a - b - c - d

        ListNode* root = new ListNode();
        root->next = head;
        // root - a - b - c - d

        ListNode* p = head;
        ListNode* q = p->next;
        // root - a - b - c - d
        //       (p) (q)

        while (q != nullptr) {
            p->next = q->next;
            // root - a - c - d
            //        b /
            q->next = root->next;
            // root - a - c - d
            //    b /
            root->next = q;
            // root - b - a - c - d
            //       (q) (p)
            q = p->next;
            // root - b - a - c - d
            //           (p) (q)
        }

        return root->next;
    }
};