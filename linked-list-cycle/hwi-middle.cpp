/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    bool hasCycle(ListNode *head) {
        if (head == nullptr)
        {
            return false;
        }
        
        unordered_set<ListNode*> ns;
        ListNode* cur = head;
        while (cur->next != nullptr)
        {
            if (ns.contains(cur))
            {
                return true;
            }

            ns.insert(cur);
            cur = cur->next;
        }

        return false;
    }
};
