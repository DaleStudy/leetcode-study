// Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

function top_k_frequent_element(numArr, k) {
  let element_qty = [];
  const numSet = [...new Set(numArr)];
  for (num of numSet) {
    const count = numArr.filter((x) => x === num).length;
    element_qty.push({ [num]: count });
  }
  Object.keys(element_qty).forEach((key) => element_qty[key]);

  const sortedArray = element_qty.sort((a, b) => {
    const valueA = Object.values(a)[0];
    const valueB = Object.values(b)[0];
    return valueB - valueA;
  });

  const topKeys = sortedArray.slice(0, k).map((obj) => Object.keys(obj)[0]);
  console.log(topKeys);
  return topKeys;
}
