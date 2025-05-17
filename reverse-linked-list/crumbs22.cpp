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
    ListNode* reverseList(ListNode* head) {
		ListNode* cur = head;
		ListNode* prv = nullptr;
		while (cur) {
			ListNode* rNode = cur->next;
			cur->next = prv;
			prv = cur;
			cur = rNode;
		}
		return (prv);
    }
};
