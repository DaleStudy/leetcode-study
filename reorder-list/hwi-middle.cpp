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

 // Editorial 코드
class Solution {
public:
    void reorderList(ListNode* head)  {
        if (head == nullptr) 
        {
            return;
        }

        ListNode* slow = head;
        ListNode* fast = head;
        while (fast != nullptr && fast->next != nullptr) 
        {
            slow = slow->next;
            fast = fast->next->next;
        }

        ListNode* prev = nullptr;
        ListNode* curr = slow;
        ListNode* tmp;
        while (curr != nullptr) 
        {
            tmp = curr->next;
            curr->next = prev;
            prev = curr;
            curr = tmp;
        }


        ListNode* first = head;
        ListNode* second = prev;
        while (second->next != nullptr) 
        {
            tmp = first->next;
            first->next = second;
            first = tmp;
            tmp = second->next;
            second->next = first;
            second = tmp;
        }
    }
};
