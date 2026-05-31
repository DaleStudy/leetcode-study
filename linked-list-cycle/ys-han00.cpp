/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
// class Solution {
// public:
//     bool hasCycle(ListNode *head) {
//         if(!head)
//             return false;
//         set<ListNode*> check;
        
//         check.insert(head);
//         while(head) {
//             if(head->next && check.find(head->next) == check.end())
//                 check.insert(head);
//             else if(head->next && check.find(head->next) != check.end())
//                 return true;
//             head = head->next;
//         }

//         return false;
//     }
// };

// class Solution {
// public:
//     bool hasCycle(ListNode *head) {        
//         while(head) {
//             if(head->val) {
//                 if(head->val == INT_MAX)
//                     return true;
//                 head->val = INT_MAX;
//             }
//             head = head->next;
//         }

//         return false;
//     }
// };

class Solution {
public:
    bool hasCycle(ListNode *head) {
        ListNode* slow = head;
        ListNode* fast = head;

        while(fast && fast->next) {
            slow = slow->next;
            fast = fast->next->next;
            if(slow == fast)
                return true;
        }

        return false;
    }
};

