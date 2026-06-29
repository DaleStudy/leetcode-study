/**
 * @param {number[]} nums
 * @return {number}
 */

/*
TC: O(n) -> for의 skip 부분을 while loop 분으로 채워짐
SC: O(n) => Set 사용
*/
var longestConsecutive = function (nums) {
  const numsSet = new Set(nums);
  let seq = 0;

  for (num of numsSet) {
    if (numsSet.has(num - 1)) continue;

    let next = num + 1;
    let currentSeq = 1;

    while (numsSet.has(next)) {
      currentSeq++;
      next++;
    }

    seq = Math.max(seq, currentSeq);
  }

  return seq;
};

/*
memory out
*/
// var longestConsecutive = function(nums) {
//     if (nums.length <= 1) return nums.length;

//     const dedupeNums = new Set(nums);

//     let maxValue = -Infinity;
//     let minValue = Infinity;
//     dedupeNums.forEach((num) => {
//         maxValue = Math.max(maxValue, num);
//         minValue = Math.min(minValue, num);
//     });

//     const markers = Array.from({ length: maxValue - minValue + 1 }, () => false);
//     let maxSequence = 0;
//     let currentSequence = 0;

//     dedupeNums.forEach((num) => {
//         markers[num - minValue] = true;
//     });

//     for (let i = 0; i < markers.length; i++) {
//         if (markers[i]) currentSequence++;
//         else {
//             maxSequence = Math.max(maxSequence, currentSequence);
//             currentSequence = 0;
//         }
//     }

//     return Math.max(maxSequence, currentSequence);
// };
