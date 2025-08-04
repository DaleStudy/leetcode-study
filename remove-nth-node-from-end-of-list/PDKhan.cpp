class Solution {
    public:
        ListNode* removeNthFromEnd(ListNode* head, int n) {
            ListNode* prev = NULL;
            ListNode* curr = head;
            ListNode* next = head;
    
            for(int i = 0; next && i < n; i++)
                next = next->next;
            
            while(next){
                if(prev == nullptr)
                    prev = head;
                else
                    prev = prev->next;
                curr = curr->next;
                next = next->next;
            }
    
            if(prev == nullptr)
                head = curr->next;
            else
                prev->next = curr->next;
    
            delete(curr);
    
            return head;
        }
    };
