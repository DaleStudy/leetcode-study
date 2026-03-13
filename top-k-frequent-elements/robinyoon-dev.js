/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number[]}
 */
var topKFrequent = function(nums, k) {
    let numsMap = new Map();

    for (let i = 0; i < nums.length; i++) {
        // 1.  numsMap에 nums[i]가 key로 있나 확인
        // 1-1. 있으면 nums[i]와 동일한 key를 찾은 후 value에 +1
        // 1-2. 없으면 새로 생성 & value를 1로.
        let hasNum = numsMap.has(nums[i]);
        if (hasNum) {
            numsMap.set(nums[i], numsMap.get(nums[i]) + 1);
        } else {
            numsMap.set(nums[i], 1);
        }
    }

    // 2. numsMap을 배열로 변경 (mapToArr)
    // 3. mapToArr에서 value가 가장 놓은 순대로 sort
    // 4. mapToArr를 k개 까지만 잘라낸 후 
    // 5. mapToArr의 각 아이템의 0번째 값만 추출하여 새로운 배열 만들고 return
    let mapToArr = Array.from(numsMap);

    mapToArr.sort((a, b) => b[1] - a[1]);

    const slicedMapToArr = mapToArr.slice(0, k);
    const result = slicedMapToArr.map((item) => item[0]);

    return result;
};
