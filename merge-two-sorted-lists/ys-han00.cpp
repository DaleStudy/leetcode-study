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
//     ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {        
//         vector<int> nums;

//         while(list1) {
//             nums.push_back(list1->val);
//             list1 = list1->next;
//         }
//         while(list2) {
//             nums.push_back(list2->val);
//             list2 = list2->next;
//         }

//         if (nums.empty()) {
//             return nullptr;
//         }

//         sort(nums.begin(), nums.end());
//         ListNode* head = new ListNode(nums[0]); 
//         ListNode* current = head;
//         for(int i = 1; i < nums.size(); i++) {
//             current->next = new ListNode(nums[i]);
//             current = current->next;
//         }
        
//         return head;
//     }
// };

class Solution {
public:
    ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {        
        ListNode* dummy = new ListNode(0);
        ListNode* current = dummy;

        while(list1 && list2) {
            if(list1->val < list2->val) {
                current->next = list1;
                list1 = list1->next;
            } else {
                current->next = list2;
                list2 = list2->next;
            }
            current = current->next;
        }

        if(list1)
            current->next = list1;
        else
            current->next = list2;

        ListNode* head = dummy->next;
        delete dummy;
        
        return head;
    }
};

