// Time complexity: O(n)
// Space complexity: O(n)

var MedianFinder = function () {
  this.arr = [];
};

/**
 * @param {number} num
 * @return {void}
 */
MedianFinder.prototype.addNum = function (num) {
  if (this.arr.length === 0) {
    this.arr.push(num);
    return;
  }

  let left = 0;
  let right = this.arr.length - 1;

  while (left <= right) {
    const mid = Math.floor((left + right) / 2);

    if (this.arr[mid] > num) {
      right = mid - 1;
      continue;
    }

    left = mid + 1;
  }

  // insert in left
  const sliced = this.arr.slice(left);
  this.arr = [...this.arr.slice(0, left), num, ...sliced];
};

/**
 * @return {number}
 */
MedianFinder.prototype.findMedian = function () {
  if (this.arr.length % 2 === 0) {
    return (
      (this.arr[this.arr.length / 2] + this.arr[this.arr.length / 2 - 1]) / 2
    );
  }

  return this.arr[(this.arr.length - 1) / 2];
};

/**
 * Your MedianFinder object will be instantiated and called as such:
 * var obj = new MedianFinder()
 * obj.addNum(num)
 * var param_2 = obj.findMedian()
 */
