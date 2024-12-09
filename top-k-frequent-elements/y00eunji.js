/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number[]}
 */
var topKFrequent = function(nums, k) {
    // 1. nums 배열을 순회하여 각 숫자의 빈도를 계산하고 obj 객체에 저장
    const obj = nums.reduce((arr, idx) => {
        arr[idx] = (arr[idx] || 0) + 1;
        return arr;
    }, {});

    // 2. obj 객체의 키-값 쌍을 배열로 변환하고, 값을 기준으로 내림차순 정렬, k개 추출
    const frequentArr = Object.entries(obj)
        .sort(([, valueA], [, valueB]) => valueB - valueA)
        .slice(0, k)
        .map(([key]) => +key);

    return frequentArr;
};
