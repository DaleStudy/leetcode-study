/**
 * @description
 * brainstorming:
 * queue
 *
 * n: length of list1 + list2
 * time complexity: O(n)
 * space complexity: O(n)
 */
var mergeTwoLists = function (list1, list2) {
  ListNode.prototype.tail = null;

  ListNode.prototype.isLast = function () {
    return this.val === 0 && this.next === null;
  };

  ListNode.prototype.pop = function () {
    const value = this.val;
    this.val = this.next ? this.next.val : 0;
    this.next = this.next ? this.next.next : null;
    return value;
  };

  ListNode.prototype.push = function (value) {
    const node = new ListNode(value);
    if (this.isLast()) {
      this.val = value;
      return;
    }

    if (this.tail === null) {
      this.next = node;
      this.tail = node;
    } else {
      this.tail.next = node;
      this.tail = node;
    }
  };

  if (list1 === null && list2 === null) return null;
  if (list1 === null || list2 === null) return list1 ? list1 : list2;

  const answer = new ListNode();

  while (!(list1.isLast() && list2.isLast())) {
    if (list1.isLast()) {
      const value = list2.pop();
      answer.push(value);
      continue;
    }
    if (list2.isLast()) {
      const value = list1.pop();
      answer.push(value);
      continue;
    }
    if (list1.val <= list2.val) {
      const value = list1.pop();
      answer.push(value);
      continue;
    }
    if (list2.val < list1.val) {
      const value = list2.pop();
      answer.push(value);
      continue;
    }
  }

  return answer;
};
