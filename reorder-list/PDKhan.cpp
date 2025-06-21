// space O(n)
class Solution {
    public:
        void reorderList(ListNode* head) {
            ListNode* search = head->next;
            ListNode* tail = head;
            deque<ListNode*> q;
    
            while(search){
                ListNode* next = search->next;
    
                search->next = NULL;
                q.push_back(search);
                search = next;
            }
    
            for(int i = 0; !q.empty(); i++){
                if(i % 2 == 0){
                    tail->next = q.back();
                    q.pop_back();
                }else{
                    tail->next = q.front();
                    q.pop_front();
                }
    
                tail = tail->next;
            }
        }
    };


// space O(1)
class Solution {
    public:
        void reorderList(ListNode* head) {
            if(head == NULL || head->next == NULL)
                return;
    
            ListNode* slow = head;
            ListNode* fast = head;
    
            while(fast->next && fast->next->next){
                slow = slow->next;
                fast = fast->next->next;
            }
    
            ListNode* prev = nullptr;
            ListNode* curr = slow->next;
    
            while(curr){
                ListNode* next = curr->next;
                curr->next = prev;
                prev = curr;
                curr = next;
            }
    
            slow->next = nullptr;
    
            ListNode* first = head;
            ListNode* second = prev;
    
            while(first && second){
                ListNode* next1 = first->next;
                ListNode* next2 = second->next;
    
                first->next = second;
                second->next = next1;
    
                first = next1;
                second = next2;
            }
        }
    };
