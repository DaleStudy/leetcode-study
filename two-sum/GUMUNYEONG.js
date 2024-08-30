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

        if (numPair[reverseKey] && parseInt(key) === numPair[reverseKey]) {
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
