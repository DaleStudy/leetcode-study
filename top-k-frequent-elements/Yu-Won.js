/**
 * 문제: https://leetcode.com/problems/top-k-frequent-elements/description/
 *
 * 요구사항:
 * nums: number[], k: number 를 Input 으로 받았을 때
 * 가장 빈도가 높은 값 k개의 값을 number[]로 리턴한다.
 *
 * * */

const topKFrequent = (nums, k) => {
    const map = new Map();

    for(let i = 0; i < nums.length; i++) {
        const count = map.get(nums[i]) || 0;
        map.set(nums[i], count+1);
    }

    const entries = [...map.entries()];
    entries.sort((a,b) => b[1]-a[1]);

    return entries.slice(0,k).map((entry) => entry[0]);
}
