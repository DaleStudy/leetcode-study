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
//     ListNode* mergeKLists(vector<ListNode*>& lists) {
//         vector<int> nums;
//         for(ListNode* list : lists) {
//             while(list != nullptr) {
//                 nums.push_back(list->val);
//                 list = list->next;
//             }
//         }

//         if(nums.size() == 0)
//             return nullptr;
        
//         sort(nums.begin(), nums.end());
//         ListNode* root = new ListNode(nums[0]);
//         ListNode* curr = root;

//         for(int i = 1; i < nums.size(); i++) {
//             curr->next = new ListNode(nums[i]);
//             curr = curr->next;
//         }

//         return root;
//     }
// };

class Solution {
public:
    ListNode* mergeKLists(vector<ListNode*>& lists) {
        priority_queue<
            pair<int, int>,
            vector<pair<int, int>>,
            greater<pair<int, int>>
        > pq;

        for(int i = 0; i < lists.size(); i++)
            if(lists[i]) 
                pq.push({lists[i]->val, i});

        ListNode dummy(-1);
        ListNode* curr = &dummy;
        while(!pq.empty()) {
            auto [val, idx] = pq.top();
            pq.pop();

            curr->next = new ListNode(val);
            curr = curr->next;

            lists[idx] = lists[idx]->next;
            if(lists[idx])
                pq.push({lists[idx]->val, idx});
        }

        return dummy.next;
    }
};

