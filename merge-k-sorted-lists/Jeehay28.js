// Priority Queue (Min-Heap) - Best for larger cases
// 🕒 Time Complexity: O(N log K), where N is the total number of nodes, K is the number of lists
// 🗂️ Space Complexity: O(K)

//
/** const PriorityQueue = require('datastructures-js').PriorityQueue;
 * // This will allow you to use the heap-based approach with a priority queue, which should be more efficient than the brute-force sorting method, especially for larger input sizes.
/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = val === undefined ? 0 : val;
 *     this.next = next === undefined ? null : next;
 * }
 */
/**
 * @param {ListNode[]} lists
 * @return {ListNode}
 */

var maxDepth = function (root) {
  // Base case: if the node is null, the depth is 0
  if (root === null) return 0;

  // Recursively calculate the depth of the left and right subtrees
  let leftDepth = maxDepth(root.left);
  let rightDepth = maxDepth(root.right);

  // Return the maximum of the two depths plus 1 for the current node
  return Math.max(leftDepth, rightDepth) + 1;
};

var mergeKLists = function (lists) {
  // Create a priority queue (min-heap) to store the nodes
  const pq = new PriorityQueue((a, b) => a.val - b.val);
  // const pq = new PriorityQueue((a, b) => b.val - a.val); <---- max-heap

  // Initialize the priority queue with the first node from each list
  for (let list of lists) {
    if (list) pq.enqueue(list); // adds the element to the back (or tail) of the queue
  }

  let dummy = new ListNode(-1);
  let current = dummy;

  // Pop nodes from the priority queue and add them to the merged list
  while (!pq.isEmpty()) {
    const node = pq.dequeue(); // removes the element from the front (or head) of the queue
    current.next = node;
    current = current.next;

    // If the current node has a next node, enqueue it
    if (node.next) pq.enqueue(node.next);
  }

  return dummy.next;
};

/**
 * ┌──────────────────────────────────────────────────────────────────────────────────────────────┐
 * │                                  Time and Space Complexity                                   │
 * ├──────────────────────────────────────────────────────────────────────────────────────────────┤
 * │ Time Complexity: O(N log K)                                                                  │
 * │  - N is the total number of nodes across all lists.                                          │
 * │  - K is the number of lists.                                                                 │
 * │  - Enqueueing and dequeueing each node from the priority queue takes O(log K) time.          │
 * │  - Since there are N nodes in total, the overall time complexity is O(N log K).              │
 * ├──────────────────────────────────────────────────────────────────────────────────────────────┤
 * │ Space Complexity: O(K)                                                                       │
 * │  - The space complexity is determined by the priority queue, which stores at most K nodes.   │
 * │  - Therefore, the space complexity is O(K), where K is the number of lists.                  │
 * ├──────────────────────────────────────────────────────────────────────────────────────────────┤
 * │ Notes:
 *   https://support.leetcode.com/hc/en-us/articles/360011833974-What-are-the-environments-for-the-programming-languages                                                                                    │
 * │  - JavaScript is run with the --harmony flag, enabling new ES6 features.                     │
 * │  - The lodash.js library is included by default in the environment.                          │
 * │  - For Priority Queue / Queue data structures, you may use:                                  │
 * │    - datastructures-js/priority-queue version 5.4.0                                          │
 * │    - datastructures-js/queue version 4.2.3                                                   │
 * │    - datastructures-js/deque version 1.04                                                    │
 * └──────────────────────────────────────────────────────────────────────────────────────────────┘
 */

// Brute Force (Array Sorting) - Good for smaller cases
// 🕒 Time Complexity: O(N log N), where N is the total number of nodes
// 🗂️ Space Complexity: O(N)

/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode[]} lists
 * @return {ListNode}
 */
var mergeKLists = function (lists) {
  const nums = [];

  // ┌──────────────────────────────────────────────────────────────────┐
  // │ Step 1: Extract values from all linked lists                     │
  // │ We traverse each linked list and push node values into 'nums'.   │
  // │ This flattens the K lists into a single array.                   │
  // └──────────────────────────────────────────────────────────────────┘
  for (let list of lists) {
    while (list) {
      nums.push(list.val);
      list = list.next;
    }
  }

  // ┌──────────────────────────────────────────────────────────────────┐
  // │ Step 2: Sort the values                                          │
  // │ JavaScript's default sort is lexicographical, so we use a custom │
  // │ comparator to sort numbers correctly in ascending order.         │
  // └──────────────────────────────────────────────────────────────────┘
  nums.sort((a, b) => a - b);

  // ┌──────────────────────────────────────────────────────────────────┐
  // │ Step 3: Create a new sorted linked list                          │
  // │ Initialize a dummy node, then iterate through the sorted array.  │
  // │ For each value, create a new ListNode and append it to the list. │
  // └──────────────────────────────────────────────────────────────────┘
  let dummy = new ListNode(-1);
  let current = dummy;

  for (num of nums) {
    current.next = new ListNode(num);
    current = current.next;
  }

  // ┌──────────────────────────────────────────────────────────────────┐
  // │ Step 4: Return the merged list                                   │
  // │ We return dummy.next since dummy is a placeholder.               │
  // └──────────────────────────────────────────────────────────────────┘
  return dummy.next;
};

/**
 * ┌──────────────────────────────────────────────────────────────────┐
 * │ Time & Space Complexity                                          │
 * ├──────────────────────────────────────────────────────────────────┤
 * │ Operation             │ Complexity                               │
 * ├──────────────────────────────────────────────────────────────────┤
 * │ Extracting values     │ O(N) - N is the total number of nodes    │
 * │ Sorting values        │ O(N log N) - JavaScript's sort uses Timsort │
 * │ Building linked list  │ O(N) - Iterates through sorted array     │
 * ├──────────────────────────────────────────────────────────────────┤
 * │ Overall Time Complexity │ O(N log N)                             │
 * ├──────────────────────────────────────────────────────────────────┤
 * │ Space Complexity      │ O(N) - Storing all node values in array  │
 * └──────────────────────────────────────────────────────────────────┘
 */
