class Solution {
    /*
    * Time Complexity: O(n)
    * Space Complexity: O(1)
    */
public:
    ListNode* reverseList(ListNode* head) {
        ListNode* prev = nullptr;
        ListNode* current = head;
        ListNode* next_temp = nullptr;

        while (current != nullptr) {
            next_temp = current->next;
            current->next = prev;
            prev = current;
            current = next_temp;
        } 
        return prev;       
    }
};
