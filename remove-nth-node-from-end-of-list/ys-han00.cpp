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
        ListNode* first = head;
        for(int i = 0; i < n; i++)
            first = first->next;
        
        ListNode* dummy = new ListNode(-1, head);
        ListNode* second = dummy;
        while(first != nullptr) {
            first = first->next;
            second = second->next;
        }

        second->next = second->next->next;
        return dummy->next;
    }

    // ListNode* removeNthFromEnd(ListNode* head, int n) {
    //     stack<ListNode*> sta;
    //     ListNode* curr = head;

    //     while(curr) {
    //         sta.push(curr);
    //         curr = curr->next;
    //     }

    //     ListNode* prev = nullptr;
    //     while(n > 1) {
    //         n--;
    //         prev = sta.top();
    //         sta.pop();
    //     }
    //     sta.pop();
    //     if(sta.empty())
    //         return prev;
    //     else {
    //         sta.top()->next = prev;
    //         return head;
    //     }
    // }
};

