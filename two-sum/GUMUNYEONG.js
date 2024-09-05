/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function (nums, target) {
    let result = [];
    let numPair = {};

    for (let i = 0; i < nums.length; i++) {
        numPair[nums[i]] = target - nums[i];
    }



    for (const key in numPair) {
        let list = [];
        const reverseKey = numPair[key];

        if (parseInt(key) === numPair[reverseKey]) {
            let firstNum;
            let secNum;

            if (parseInt(key) === reverseKey) {
                firstNum = nums.indexOf(reverseKey);
                secNum = nums.indexOf(reverseKey, firstNum + 1);
            } else {
                firstNum = nums.indexOf(parseInt(key));
                secNum = nums.indexOf(reverseKey);
            }

            result.push(firstNum);
            result.push(secNum);

            return result;
        }
    }

};

// TC : O(n)
// 1. num 을 순회하며 numPair 객체를 만듦(num 길이 n)
// 2. numPair 를 순회하며 키-값이 대칭되는 첫번째 쌍을 찾음 (numPair 길이 n)
// 3. num을 순회하며 인덱스를 찾음 (num 길이 n)
// O(3n) 따라서 시간복잡도는 O(n)

// SC : O(n)
// 크기가 n만큼인 객체(numPair)를 생성하므로 공간 복잡도도 O(n)

