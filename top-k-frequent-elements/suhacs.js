// Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

function top_k_frequent_element(numArr, k) {
  let element_qty = [];
  const numSet = [...new Set(numArr)];
  for (num of numSet) {
    const count = numArr.filter((x) => x === num).length;
    element_qty.push({ [num]: count });
  }
  Object.keys(element_qty).forEach((key) => element_qty[key]);
}

const Arr = [1, 2, 3, 4, 5, 5, 5, 5, 3, 3, 32, 2, 2, 1];
top_k_frequent_element(Arr);
