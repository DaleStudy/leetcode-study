class Solution {
    public:
        ListNode* reverseList(ListNode* head) {
            ListNode* new_head = NULL;
            ListNode* curr = head;
    
            while(curr){
                ListNode* next = curr->next;
    
                curr->next = new_head;
                new_head = curr;
                curr = next;
            }
    
            return new_head;
        }
    };
