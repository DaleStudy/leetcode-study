/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* reverseList(struct ListNode* head) {

    struct ListNode* ptr1 = NULL;
    struct ListNode* ptr2 = head;
    struct ListNode* ptr3 = NULL;

    while (ptr2 != NULL) {
        ptr3 = ptr2->next;
        ptr2->next = ptr1;

        // 앞으로 전진
        ptr1 = ptr2;
        ptr2 = ptr3;
    }
    return ptr1;
}
// 시간 복잡도: O(노드 개수)
// 공간 복잡도: O(1)
