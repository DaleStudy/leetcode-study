struct Compare{
    bool operator()(ListNode* a, ListNode* b){
        return a->val > b->val;
    }
};

class Solution {
public:
    ListNode* mergeKLists(vector<ListNode*>& lists) {
        priority_queue<ListNode*, vector<ListNode*>, Compare> pq;
        ListNode* head = nullptr;
        ListNode* tail;

        for(ListNode* node : lists){
            if(node) pq.push(node);
        }

        while(!pq.empty()){
            ListNode* node = pq.top();

            pq.pop();
            if(head == nullptr){
                head = node;
                tail = head;
            }else{
                tail->next = node;
                tail = tail->next;
            }

            if(node->next)
                pq.push(node->next);
        }

        return head;
    }
};
