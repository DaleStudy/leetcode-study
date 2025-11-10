/**
 * 정수 배열 두 숫자를 합쳐서 target의 값이 나오게 해야함
 * 해당하는 인덱스를 길이가 2인 배열로 반환하시오.
 * 각 정수는 한 번씩만 쓸 수 있음.
 * 
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    const numsMap = new Map();

    nums.forEach((num, i) => {
        if(!numsMap.has(num)) numsMap.set(num, []);
        numsMap.get(num).push(i);
    });
    
    for(let i = 0; i < nums.length; i ++) {
        for(let j = i + 1; j < nums.length; j ++) {
            if(nums[i] + nums[j] === target) {
                if(hasMultipleEntries(numsMap.get(nums[i]))) {
                    return [...numsMap.get(nums[i]).slice(0,2)];
                } else {
                    return [...numsMap.get(nums[i]), ...numsMap.get(nums[j])];
                }
            }
        }
    }

    return;
};

function hasMultipleEntries(arr) {
    return arr.length >= 2;
}