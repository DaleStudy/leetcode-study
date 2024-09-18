/**
 * @description
 * brainstorming:
 * Thinking of stacking nodes like stacks while traveling
 *
 * time complexity: O(n)
 * space complexity: O(n)
 */

var reverseList = function (head) {
  let answer = null;

  const search = (target) => {
    if (target === null) return;

    const node = new ListNode(target.val, answer);
    answer = node;

    search(target.next);
  };

  search(head);

  return answer;
};
