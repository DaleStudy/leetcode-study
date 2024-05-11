var reverseList = function(head) {
    let current = head;
    let previous = null;

    // iterates through the linked list nodes.
    while(current){
        // stores the next node of current.
        const next = current.next;
        // reverses the direction of the pointer of current to point to the previous node.
        current.next = previous;
        // updates previous to be the current node.
        previous = current;
        // moves current to the next node.
        current = next;
    }

    return previous;
};

// Time complexity : O(n)
// Space complexity : O(1)
