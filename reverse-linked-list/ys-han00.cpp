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
// class Solution {
// public:
//     ListNode* reverseList(ListNode* head) {
//        if(!head || !head->next)
//            return head;

//         ListNode* curr = head;
//         ListNode* next = head->next;
//         curr->next = nullptr;

//         while(next) {
//             ListNode* temp = next->next;
//             next->next = curr;

//             curr = next;
//             next = temp;
//         }
        
//         return curr;
//     }
// };

// class Solution {
// public:
//     ListNode* rec(ListNode* old, ListNode* now) {
//         if(!now->next) {
//             now->next = old;
//             return now;
//         }
//         ListNode* tmp = now->next;
//         now->next = old;
//         return rec(now, tmp);
//     }
//     ListNode* reverseList(ListNode* head) {
//        if(!head || !head->next)
//            return head;

//         ListNode* ans = rec(head, head->next);
//         head->next = nullptr;
        
//         return ans;
//     }
// };

class Solution {
public:
    ListNode* reverseList(ListNode* head) {
        if(!head || !head->next)
            return head;

        ListNode* new_tail = head->next;
        ListNode* new_head = reverseList(new_tail);
        new_tail->next = head;
        head->next = nullptr;
        
        return new_head;
    }
};

