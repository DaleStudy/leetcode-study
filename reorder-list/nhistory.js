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
