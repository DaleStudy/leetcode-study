
/**
 * 최장 증가 부분 수열을 계산
 * @param {number[]} nums 
 * @returns {number} - 조건을 만족하는 수열의 최대 길이
 * 
 * 시간 복잡도: O( n log(n) )
 *   - n은 배열의 길이
 *   - 각 요소를 처리할 때 이분 탐색으로 위치를 찾기 때문에 log(n)이 소요됨
 * 공간 복잡도: O(n)
 *  - 배열에 최대 n개의 요소를 저장 가능
 */
function lengthOfLIS(nums: number[]): number {
    // 수열을 저장할 배열
    const sequnces: number[] = [];

    for (let num of nums) {
        // 이분 탐색을 사용하여 num이 들어갈 위치름 찾음
        let left = 0;
        let right = sequnces.length;

        while (left < right) {
            const mid = Math.floor((left + right) / 2);
            if (sequnces[mid] < num) {
                left = mid + 1;
            } else {
                right = mid;
            }
        }

        // 새로운 요소를 추가하거나 기존 요소를 대체
        if (left < sequnces.length) {
            sequnces[left] = num;
        } else {
            sequnces.push(num)
        }
    }

    return sequnces.length;
}

