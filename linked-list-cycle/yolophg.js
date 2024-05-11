var hasCycle = function(head) {
    // check to ensure that the head exists and if head is null or if there's only one, return false.
    if (!head || !head.next) {
       return false;
   }

   let slow = head;
   let fast = head.next;

   // iterates through the linked list looking for a cycle.
   while (fast && fast.next) {
       if (slow === fast) {
           return true; 
       }
       // if the pointers haven't met yet, slow pointer moves one step forward.
       slow = slow.next;
       // fast pointer moves two steps forward.
       fast = fast.next.next;
   }

   return false;
};

// Time complexity : O(n)
// Space complexity : O(1)
