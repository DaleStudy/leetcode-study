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
//풀이 참고하였음.
class Solution {
public:
    ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) { //list1, list2 다 포인터
        ListNode mergedNode(-1); //mergedNode 객체 선언
        ListNode* mergedNodeList = &mergedNode; //node: (merged 객체)의 (주소) (&merged)저장 (객체를 포인터에 넣기)

        ListNode* l1 = list1; // 포인터 l1
        ListNode* l2 = list2; // 포인터 l2

        while (l1 != nullptr && l2 != nullptr) {
            //l1, l2 둘 중에 head 값(->val) 값이 작은 것을 node->next에 연결
            if (l1->val < l2->val) { // 포인터로 객체의 속성 참조(->)
                mergedNodeList->next = l1;
                l1 = l1->next;
            } else {
                mergedNodeList->next = l2;
                l2 = l2->next;
            }
            mergedNodeList = mergedNodeList->next;
        }

        //남아있는 list를 node->next에 연결
        mergedNodeList->next = (l1 != nullptr) ? l1 : l2;
        //return the head of the merged linked list (mergeNode -1 다음 것을 가리키는 포인터 next)
        return mergedNode.next;

    }
};
