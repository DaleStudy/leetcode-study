/**
 * @param {number[]} nums
 * @return {number}
 */
var rob = function (nums) {
    if (nums.length === 1) {
        return nums[0];
    }

    const dp1 = [0, nums[0]];
    const dp2 = [0, 0];

    for (let i = 1; i < nums.length; i++) {
        const prevIndex = i - 1;

        const dp1Max = Math.max(dp1[prevIndex] + nums[i], dp1[i]);
        dp1.push(dp1Max);

        const dp2Max = Math.max(dp2[prevIndex] + nums[i], dp2[i]);
        dp2.push(dp2Max);
    }

    return Math.max(dp1[dp1.length - 2], dp2[dp2.length - 1])
};

// 시간복잡도 O(n) -> nums의 길이만큼 for문에서 최대값을 dp계산
// 공간복잡도 O(n) -> nums의 길이만큼 dp배열에 원소가 추가됨
