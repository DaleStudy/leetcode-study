/**
 * 문제: https://leetcode.com/problems/contains-duplicate/
 *
 * 요구사항:
 * nums: number[]를 Input 으로 받았을 때
 * 중복된 값이 있을 경우 true 없다면 false 를 반환
 *
 * 해시맵 이용
 * */

const containsDuplicate = (nums) => {
    const set = new Set();

    for(const num of nums) {
        if(set.has(num)) {
            return true;
        }
        set.add(num);
    }
    return false;

}