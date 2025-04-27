#include <iostream>

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
        ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {
            if (!list1)
                return (list2);
            if (!list2)
                return (list1);
    
            ListNode ans_head = ListNode();
            ListNode* tmp = &ans_head;
    
            while (list1 && list2) {
                if (list1->val <= list2->val) {
                    tmp->next = list1;
                    list1 = list1->next;
                    tmp = tmp->next;
                }
                else {
                    tmp->next = list2;
                    list2 = list2->next;
                    tmp = tmp->next;
                }
            }
            if (list1) {
                tmp->next = list1;
            }
            else if (list2) {
                tmp->next = list2;
            }
            return (ans_head.next);
        }
    };
