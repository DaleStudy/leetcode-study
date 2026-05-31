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
private:
    struct cmp
    {
        bool operator() (ListNode* a, ListNode* b)
        {
            return a->val > b->val;
        }
    };

public:
    ListNode* mergeKLists(vector<ListNode*>& lists) {
        if (lists.empty())
        {
            return nullptr;
        }

        priority_queue<ListNode*, vector<ListNode*>, cmp> pq;

        for (ListNode* list: lists)
        {
            while (list != nullptr)
            {
                pq.push(list);
                list = list->next;
            }
        }

        if (pq.empty())
        {
            return nullptr;
        }

        ListNode* res = pq.top();
        ListNode* prev = res;
        while (!pq.empty())
        {
            ListNode* n = pq.top();
            pq.pop();
            prev->next = n;
            prev = n;
        }

        prev->next = nullptr;

        return res;
    }
};
