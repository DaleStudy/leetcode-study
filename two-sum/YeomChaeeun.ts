/**
 * 배열 두 수의 합이 target 과 같은 값
 * 알고리즘 복잡도:
 * - 시간복잡도: O(n^2)
 * - 공간복잡도: O(1)
 * @param nums
 * @param target
 */
function twoSum(nums: number[], target: number): number[] {
    let result: number[] = [];

    for(let i = 0; i < nums.length; i++) {
        for(let j = i + 1; j < nums.length; j++) {
            if(nums[i] + nums[j] === target) {
                result.push(i, j);
                return result;
            }
        }
    }
}
