/**
 * @description
 * brainstorming:
 * hash table
 *
 * n = length of head
 * time complexity: O(n)
 * space complexity: O(n)
 */
var hasCycle = function (head) {
  const set = new Set();
  let node = head;

  while (node) {
    if (set.has(node)) return true;
    set.add(node);
    node = node.next;
  }

  return false;
};
