/**
 * @description
 * queue의 특성을 활용하여 풀이
 *
 * n = length of lists
 * m = length of lists[i]
 * time complexity: O(n * n * m)
 * space complexity: O(n*m)
 */
var mergeKLists = function (lists) {
  let answer = null;
  let tail = null;
  let totalSize = lists.reduce((size, list) => {
    let head = list;
    let count = 0;

    while (head) {
      head = head.next;
      count++;
    }

    return size + count;
  }, 0);

  while (totalSize--) {
    let minIndex = lists.reduce((acc, list, i) => {
      if (list === null) return acc;
      if (acc === null) return { value: list.val, index: i };
      return acc.value < list.val ? acc : { value: list.val, index: i };
    }, null).index;

    if (answer === null) {
      answer = lists[minIndex];
      tail = answer;
    } else {
      tail.next = lists[minIndex];
      tail = lists[minIndex];
    }

    lists[minIndex] = lists[minIndex].next;
  }
  return answer;
};
