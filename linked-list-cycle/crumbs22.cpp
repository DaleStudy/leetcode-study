/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */

/*
    해시 (std::unordered_set<>)에 주소를 기록해두고,
        다음 노드로 넘어가기 전에 이미 집합에 들어있는지 검사

    공간복잡도는 O(n)으로, 해시에 대한 메모리를 사용
    시간복잡도는 O(n)
*/


class Solution {
public:
    bool hasCycle(ListNode *head) {
        std::unordered_set<ListNode*> visited;
        ListNode* cur = head;

        while (cur) {
            if (visited.count(cur) == 1) // 이미 본 노드면 cycle이 존재
                return (true) ;
            
            visited.insert(cur); // 방문 기록
            cur = cur->next;
        } 
        return (false); // 끝까지 돌았으나 순환이 없는 경우에만 cycle이 존재하지 않음
    }
};
