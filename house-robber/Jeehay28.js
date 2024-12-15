/**
 * @param {number[]} nums
 * @return {number}
 */

//  Bottom-Up DP (with constant space) 방식 

// 시간 복잡도 (Time Complexity)
// O(n) — 입력 배열의 크기에 비례하여 수행 시간이 증가

// 공간 복잡도 (Space Complexity)
// O(1) — 입력 크기에 관계없이 사용하는 메모리 공간이 일정


var rob = function (nums) {

    if (nums.length === 1) {
        return nums[0];
    }

    let robbed_2 = nums[0];
    let robbed_1 = Math.max(nums[0], nums[1]);

    for (let i = 2; i < nums.length; i++) {

        const temp = robbed_1;

        robbed_1 = Math.max(robbed_1, robbed_2 + nums[i]);

        robbed_2 = temp;

    }

    return robbed_1;

};
