/**
 * 문제: https://leetcode.com/problems/longest-consecutive-sequence/description/
 *
 * 요구사항:
 * 정렬되지 않은 nums: number[]를 Input 으로 받았을 때
 * 가장 긴 연속으로 된 값의 length 를 반환한다.
 * 단 O(n) 이어야한다.
 *
 * * */

const longestConsecutive = (nums) => {
    const set = new Set(nums);
    let count = 0;

    for(let num of set) {
        if(!set.has(num-1)) {
            let len = 1;

            while (set.has(num+len)) {
                len++;
            }

            count = Math.max(count, len);
        }
    }
    return count;
}
