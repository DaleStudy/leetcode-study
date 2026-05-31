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
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        // 스택에 넣고 뒤집어서 n번째 노드 찾기
        stack<ListNode*> s;
        ListNode* cur = head;
        while (cur != nullptr)
        {
            s.push(cur);
            cur = cur->next;
        }

        for (int i = 0; i < n; ++i)
        {
            cur = s.top();
            s.pop();
        }

        // 스택이 빌 때 까지 pop한 경우는 head를 제거하는 경우
        if (s.empty())
        {
            return head->next;
        }

        // 그 외에는 prev가 존재
        ListNode* prev = s.top();
        prev->next = cur->next;
        return head;
    }
};
