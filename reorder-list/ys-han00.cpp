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
    void reorderList(ListNode* head) {
        ListNode* slow = head;
        ListNode* fast = head;
        while (fast->next && fast->next->next) {
            slow = slow->next;
            fast = fast->next->next;
        }

        ListNode* curr = slow->next;
        slow->next = nullptr; 
        ListNode* prev = nullptr;
        
        while (curr) {
            ListNode* temp = curr->next;
            curr->next = prev;
            prev = curr;
            curr = temp;
        }

        ListNode* first = head;
        ListNode* second = prev;
        
        while (second) {
            ListNode* temp1 = first->next;
            ListNode* temp2 = second->next;

            first->next = second;
            second->next = temp1;

            first = temp1;
            second = temp2;
        }
    }

    // void reorderList(ListNode* head) {
    //     ListNode* now = head;
    //     stack<ListNode*> sta;

    //     while(now) {
    //         sta.push(now);
    //         now = now->next;
    //     }

    //     now = head;
    //     int n = sta.size();
    //     for(int i = 0; i < n / 2; i++) {
    //         ListNode* tail = sta.top();
    //         sta.pop();

    //         tail->next = now->next;
    //         now->next = tail;
    //         now = tail->next;
    //     }

    //     now->next = nullptr;
    // }

    // void reorderList(ListNode* head) {
    //     ListNode* now = head;
    //     stack<ListNode*> sta;

    //     while(now) {
    //         sta.push(now);
    //         now = now->next;
    //     }

    //     now = head;
    //     int cnt = 0;
    //     int node_cnt = sta.size();
    //     while(cnt < node_cnt / 2) {
    //         if(cnt != node_cnt / 2 - 1)
    //             sta.top()->next = now->next;
    //         else {
    //             if(node_cnt & 1) {
    //                 now->next->next = nullptr;
    //                 sta.top()->next = now->next;
    //             }
    //             else
    //                 sta.top()->next = nullptr;
    //         }
    //         now->next = sta.top();
    //         now = sta.top()->next;
    //         sta.pop();
    //         cnt++;
    //     }
    // }
};

