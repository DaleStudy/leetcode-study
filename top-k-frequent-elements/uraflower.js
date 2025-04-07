/**
 * 주어진 배열에서 가장 많이 속해있는 숫자 k개를 반환하는 함수
 * @param {number[]} nums
 * @param {number} k
 * @return {number[]}
 */
const topKFrequent = function(nums, k) {
    const count = {};
    nums.forEach((num) => {
        count[num] = count[num] + 1 || 1;
    });
    return Object.keys(count).sort((a, b) => count[b] - count[a]).slice(0, k).map(Number);
};

// 시간복잡도: O(n)
// 공간복잡도: O(n)
