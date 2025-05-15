/*
    풀이 :
        linked-list를 순회하며 stack에 차례대로 push하고 다 넣은 후
        pop하면서 역순으로 연결해준다

    노드의 개수 : N

    TC : O(N)
        총 2회 while 반복문 O(N + N)
    
    SC : O(N)
        스택은 노드의 개수에 비례
*/

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

#include <stack>
using namespace std;

struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

class Solution {
    public:
        ListNode* reverseList(ListNode* head) {
            stack<ListNode*>    st;
            ListNode    dummy;
            ListNode*   prv = &dummy;
            ListNode*   cur;
    
            while (head)
            {
                st.push(head);
                head = head->next;
            }
    
            while (!st.empty())
            {
                cur = st.top();
                prv->next = cur;
                prv = cur;
                st.pop();
            }
            prv->next = nullptr;
            
            return dummy.next;
        }
    };
