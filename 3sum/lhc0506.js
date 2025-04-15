/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var threeSum = function(nums) {
    const result = [];
    const numsMap = {};

    nums.forEach((num, index) => {
        numsMap[num] = (numsMap[num] || 0) + 1;

    });

    for (let i = 0; i < nums.length - 1; i++) {
        for (let j = i + 1; j < nums.length; j++) {
            const a = nums[i];
            const b = nums[j];
            const targetNum = -(a + b);

            if (!numsMap[targetNum]) {
                continue;
            }

            if ((targetNum === a || targetNum === b) && numsMap[targetNum] === 1) {
                continue;
            }

            if (targetNum === a && targetNum === b && numsMap[targetNum] <= 2) {
                continue;
            }

            const triplet = [a, b, targetNum].sort((x, y) => x - y);
            const key = triplet.join(',');

            if (seen.has(key)) {
                continue;
            }

            seen.add(key);

            result.push(triplet);
        }
    }

    return result;
};


//시간 복잡도 O(n²) , 공간 복잡도 O(n²) 라고 생각했는데 Time Limit Exceeded 에러 발생
// 추후 다시 풀어볼 예정
