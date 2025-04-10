/**
 * @param {number[]} nums
 * @return {number[][]}
 *
 * 풀이 1
 *
 * 이렇게 푸니까 시간복잡도 O(n^3) / 공간복잡도 O(n) 라서 복잡한 예시에는 time limit 이 발생함
 * 개선해보자..
 *
 * function threeSum(nums: number[]): number[][] {
 *  nums.sort((a, b) => a - b);
 *     let result = []
 *     for (let i= 0; i<nums.length; i++){
 *         for(let j= i+1 ; j <nums.length; j++){
 *             for (let k = j+1; k<nums.length; k++){
 *                 if(nums[i]+nums[j]+nums[k]===0){
 *                     result.push([nums[i], nums[j], nums[k]]);
 *                 }
 *             }
 *         }
 *     }
 *
 *     return Array.from(
 *         new Set(result.map(item => JSON.stringify(item))),
 *         str => JSON.parse(str)
 *     );
 *     }
 *
 *  풀이 2
 *
 *  투포인터를 활용해보자.
 *  아래처럼 문제를 풀게되면 시간복잡도 O(n^2) / 공간복잡도 O(1) 이다.
 *  시공간 복잡도가 줄긴하지만 메모리 사용량과 큰 숫자를 다룰 때 성능이 매우 좋다!
 */


function threeSum(nums: number[]): number[][] {
    let result : number[][] = []
    nums.sort((a, b) => a - b);
    const n = nums.length;

    for(let first = 0; first<n-2; first++){
        // 첫번째가 양수면 0이 될 수 없음
        if(nums[first] > 0) break;

        //중복된 수는 건너뜀
        if(first > 0 && nums[first]===nums[first-1]) continue;

        let left = first + 1;
        let right = n-1;

        while(left < right){
            const sum = nums[first] +nums[left] + nums[right];

            if(sum < 0){
                left ++
            }else if(sum > 0){
                right --;
            }else{
                result.push([nums[first],nums[left],nums[right]]);
                // left, left+1 이 같을 때 중복된 수는 건너뜀
                while(left < right && nums[left] === nums[left+1]) left++;
                // right, right+1 이 같을 때 중복된 수는 건너뜀
                while(left < right && nums[right] === nums[right-1]) right--;
                left++;
                right--;
            }
        }
    }
    return result;
}
