/*
    풀이 :
        최소힙을 사용해서 풀이한다
        리스트의 각 맨앞 노드를 최소힙에 넣고 최소 값을 가진 노드를 dummy에 붙여나간 뒤 next를 다시 최소힙에 넣는 것을 반복

    노드의 개수 : N, list의 개수 K

    TC : O (N log K)
        K개의 크기를 가지는 최소 힙에 넣고 제거하는 시간 -> logK * 모든 노드에 대한 순회 N

    SC : O (K)
        최소힙 크기는 K에 비례
*/

#include <vector>
#include <queue>

using namespace std;

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

struct cmp {
    bool    operator()(const ListNode* a, const ListNode* b) {
        return a->val > b->val;
    }
};

class Solution {
public:
    ListNode* mergeKLists(vector<ListNode*>& lists) {
        priority_queue<ListNode*,  vector<ListNode*>, cmp> pq;

        for (auto list : lists) {
            if (list)
                pq.push(list);
        }

        ListNode dummy, *tail = &dummy;

        while (!pq.empty()) {
            ListNode* minNode = pq.top(); pq.pop();

            if (minNode->next)
                pq.push(minNode->next);

            tail->next = minNode;
            tail = minNode;
        }
        return dummy.next;
    }
};
