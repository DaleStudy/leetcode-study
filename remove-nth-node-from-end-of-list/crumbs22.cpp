/*
    노드의 개수 cnt를 세고, n과 cnt를 통해 움직여야 할 위치 mv를 계산한다
    mv가 0일 때 첫번째 노드를 제거하므로 head->next를 반환
    mv가 0이 아닐 때는 head부터 mv만큼 이동한 후, 그 노드의 이전 노드(fh)와 다음 노드(tmp->next)를 연결한다
    시간복잡도는 O(n)이고 추가적인 공간은 사용하지 않으므로 공간복잡도는 O(1)이다
*/
class Solution {
public:
    ListNode* removeNthFromEnd(ListNode* head, int n) {

        int cnt = 0;
        ListNode* end = head;
        while (end) {
            end = end->next;
            cnt++;
        }

        int mv = cnt - n;
        if (mv == 0)
            return (head->next);
        ListNode* fh = nullptr;
        ListNode* tmp = head;
        for (int i = 0; i < mv; i++) {
            fh = tmp;
            tmp = tmp->next;
        }
        if (!fh)
            return (nullptr);
        if (tmp->next)
            fh->next = tmp->next;
        else
            fh->next = nullptr;
        return (head);
    }
};
