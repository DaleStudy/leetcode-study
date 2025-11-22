/**
 * @param {number[]} nums
 * @return {number[]}
 */
var productExceptSelf = function (nums) {

    const NUMS_LENGTH = nums.length;
    const isZeroArray = []; //boolean
    let zeroCount = 0;

    let totalProduct = nums.reduce((acc, item) => {
        if (item === 0) {
            zeroCount++;
            isZeroArray.push(true);
            return acc;
        } else {
            isZeroArray.push(false);
            return acc * item;
        }
    }, 1);

    // 엣지 케이스 대비 1: nums의 요소 중 0이 두 개 이상인 경우
    if (zeroCount >= 2) {
        totalProduct = 0;
    }

    const tempArray = [];

    for (let i = 0; i < NUMS_LENGTH; i++) {
        if (isZeroArray[i] === true) {
            tempArray.push(totalProduct);
        } else if (zeroCount >= 1) {
            // 엣지 케이스 대비 2: isZeroArray[i]가 false 더라도 nums의 요소 중 zero가 하나라도 있는 경우
            // (지금 보니 이 부분은 zeroCount === 1로 했어도 될 것 같네요...)
            tempArray.push(0);
        } else {
            tempArray.push(totalProduct / nums[i]);
        }
    }

    return tempArray;
};

