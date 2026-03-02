/**
 * 문제: https://leetcode.com/problems/two-sum/
 *
 * 요구사항:
 * nums: number[], target: number 를 Input 으로 받았을 때
 * nums에 있는 값 두개를 더했을 때 target 과 정확하게 일치하게 되는 값을 만들게 되는 인덱스 배열을 리턴한다.
 *
 * 해시맵 이용
 * */

const twoSum = (nums, target) => {
    const map = new Map();

    for(let i = 0; i < nums.length; i++) {
        const result = target - nums[i];

        // 이미 값이 있었다면 리턴
        if(map.has(result)) {
            return [map.get(result), i];
        }

        // 현재 값을 저장
        map.set(nums[i], i);
    }
}