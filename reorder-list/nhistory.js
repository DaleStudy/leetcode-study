// First option : change node value
var reorderList = function (head) {
  if (!head) return;
  // Create new arr to return result and current head
  let arr = [];
  let curr = head;
  // Make list array that has every values from linked list
  let list = [];
  while (curr) {
    list.push(curr.val);
    curr = curr.next;
  }
  // Iterate list array if i%2 === 0 then curr.val = list[Math.floor(i / 2)]
  // If i%2 !== 0 them curr.val = list[list.length - Math.floor((i + 1) / 2)]
  curr = head;
  for (let i = 0; i < list.length; i++) {
    if (i % 2 === 0) {
      curr.val = list[Math.floor(i / 2)];
    } else {
      curr.val = list[list.length - Math.floor((i + 1) / 2)];
    }
    curr = curr.next;
  }
};

// TC: O(n)
// SC: O(n)

// Second option : move node without changing values
var reorderList = function (head) {
  // Edge case
  if (!head) return;

  // Find mid node from linked list
  let slow = head,
    fast = head;
  while (fast && fast.next) {
    slow = slow.next;
    fast = fast.next.next;
  }

  // Reverse second half list
  let prev = null,
    curr = slow,
    temp;
  while (curr) {
    temp = curr.next;
    curr.next = prev;
    prev = curr;
    curr = temp;
  }

  // Modify linked list as followed instruction
  let first = head,
    second = prev;
  while (second.next) {
    temp = first.next;
    first.next = second;
    first = temp;

    temp = second.next;
    second.next = first;
    second = temp;
  }
};

// TC: O(n)
// SC: O(1)
