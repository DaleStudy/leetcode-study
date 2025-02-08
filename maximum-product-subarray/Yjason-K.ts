/**
 * subArray 중 최대 곱을 구하는 함수
 * @param {number[]} nums - 숫자 배열 
 * @returns {number} - subArray 중 최대 곱
 * 
 * @description 음수의 곱이 존재 할 수 있기 때문에, 최대 값과 최소값을 갱신하며, 결과 값을 갱신.
 * 
 * 시간 복잡도 : O(n)
 *  - nums 배열 1회 순회
 * 
 * 공간 복잡도 : O(1)
 */
function maxProduct(nums: number[]): number {
    let max = nums[0];
    let min = nums[0];
    let result = nums[0];
    
    // 첫 번째 요소를 제외한 모든 요소를 탐색
    for (let i = 1; i < nums.length; i++) {  
        let current = nums[i]

        // 현재 값, 이전 최대 곱과의 곱, 이전 최소 곱과의 곱 중 최대/최소 갱신
        const cases = [current * max, current * min, current];

        max = Math.max(...cases);
        min = Math.min(...cases);
        result = Math.max(result, max);
    }
    
    return result;
}

