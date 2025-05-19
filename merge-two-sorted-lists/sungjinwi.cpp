/*
    풀이 :
        dummy를 맨 앞에 세우고 list1과 list2의 맨 앞 성분 value를 비교하며 dummy 뒤에 노드를 이어줌
        이어준 list는 next로 전진시키면서 계속 반복문
        둘 중 하나가 null이 되면 남은 리스트 전체를 맨 뒤에 이어줌

    리스트 길이 : M, N

    TC : O(M + N)
        번갈아서 나올 경우 두 리스트 전체의 길이에 비례

    SC : O(1)
        기존 노드를 활용하므로 추가적인 메모리는 dummy와 tmp만 사용한다
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
class Solution {
    public:
        ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {
            ListNode    dummy;
            ListNode    *tmp;

            tmp = &dummy;
            while (list1 && list2)
            {
                if (list1->val <= list2->val)
                {
                    tmp->next = list1;
                    list1 = list1->next;
                }
                else
                {
                    tmp->next = list2;
                    list2 = list2->next;
                }
                tmp = tmp->next;
            }
            if (list1)
                tmp->next = list1;
            else
                tmp->next = list2;
            return dummy.next;
        }
    };
