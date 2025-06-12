/*
    풀이 :
        투포인터 기법을 이용해 중간 노드를 구해 리스트를 반으로 나누고 뒤의 그룹은 순서를 뒤집는다
        번갈아가면서 다시 붙여준다
    
    노드 총 개수 : N

    TC : O(N)

    SC : O(1)
*/

class Solution {
    public:
        void reorderList(ListNode* head) {
            ListNode *slow = head, *fast = head;
    
            while (fast && fast->next) {
                slow = slow->next;
                fast = fast->next->next;
            }
            
            ListNode *prev = nullptr, *curr = slow->next;
            slow->next = nullptr;
    
            while (curr) {
                ListNode *tmp = curr->next;
                curr->next = prev;
                prev = curr;
                curr = tmp;
            }
    
            ListNode *first = head, *second = prev;
            while (second) {
                ListNode *tmp1 = first->next, *tmp2 = second->next;
                first->next = second;
                second->next = tmp1;
                first = tmp1;
                second = tmp2;
            }
        }
    };

struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};
