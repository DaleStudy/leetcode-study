/**
 * 주어진 숫자 배열에서 가장 긴 연속된 수열의 길이를 찾는다.
 * 시간복잡도: O(n)
 * 이유: 각 숫자는 최대 한 번만 시작점으로 검사되고,
 * 연속 수열 탐색도 중복 없이 진행된다.
 * 
 * @param {number[]} nums
 * @return {number}
 */
var longestConsecutive = function(nums) {

    // 배열을 Set으로 변환
    const numSet = new Set(nums);

    // 가장 긴 연속 길이를 저장
    let longest = 0;
    // Set을 순회
    for (let n of numSet) {
        // 현재 숫자가 연속 수열의 "시작점"인지 확인
        // n-1 이 존재하면 이미 앞에 전 수열 존재함
        if (!numSet.has(n - 1)) {

            // 시작하는 수열 길이
            let length = 1;

            // 계속 존재하는지 확인
            while (numSet.has(n + length)) {
                length++;
            }
            // 지금까지 찾은 최대 길이 갱신
            longest = Math.max(longest, length);
        }
    }
    return longest;   
};
