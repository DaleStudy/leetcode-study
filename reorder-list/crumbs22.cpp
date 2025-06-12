/*
	큐와 스택구조를 활용해 노드의 주소를 각각 저장해놓고
	큐에서 한 번, 스택에서 한 번 요소를 빼와서 재정렬한다
	링크드리스트를 한 번 순회하면서 push하고 같은 길이만큼 한 번 더 순회하므로 O(2n)의 시간복잡도와
	노드 길이만큼의 자료구조를 2개 더 사용하므로 O(2n)의 공간복잡도를 사용
*/

class Solution {
public:
    void reorderList(ListNode* head) {
        ListNode* tmp = head;
        queue<ListNode*> q;
        stack<ListNode*> s;

        while (tmp) {
            s.push(tmp);
            q.push(tmp);
            tmp = tmp->next;
        }

        // 큐 - 스택 - 큐 - 스택 ...
        // 큐는 앞에서 1/2을, 스택은 뒤에서 1/2을 반복하며 요소 추출
        int len = q.size();
        tmp = q.front();
        q.pop();

        for (int i = 0; i < len / 2; i++) {
            tmp->next = s.top();
            s.pop();
            tmp = tmp->next;
            tmp->next = q.front();
            q.pop();
            tmp = tmp->next;
        }
        tmp->next = nullptr;

    }
};
