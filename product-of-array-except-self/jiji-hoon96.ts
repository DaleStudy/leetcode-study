/**
 *
 * 풀이 1
 *
 * 아래와 같이 문제를 푸니, 성능적으로 문제가 발생했다.
 * 시간복잡도는 0(n2) / 공간 복잡도는 0(n)
 *
 * function productExceptSelf(nums: number[]): number[] {
 *     if(nums.every(num => num === 0)) return nums; 시간 복잡도 0(n)
 *     if(nums.length > 2 && nums.filter(num=> num ===0).length > 1) return new Array(nums.length).fill(0) 시간 복잡도 0(n) 공간 복잡도 0(n)
 *     let result = [] 공간 복잡도 0(n)
 *     for(let i =0;i<nums.length; i++){ 시간 복잡도 0(n)
 *         let multi = 1;
 *         const a= nums.filter((num,index)=> index !== i); 시간 복잡도 0(n) 공간 복잡도 0(n)
 *         for(let item of a){ 시간 복잡도 0(n)
 *             multi *= item
 *         }
 *         result.push(multi)
 *     }
 *     return result
 * };
 *
 * 풀이 2 는 누적합 알고리즘을 사용해서 왼쪽 방향에서 시작해 오른쪽 방향으로 곱하는 방식으로 문제 해결
 *
 */

function productExceptSelf(nums: number[]): number[] {
    const n = nums.length;
    const result = new Array(n).fill(1);

    let leftProduct = 1;
    for (let i = 0; i < n; i++) {
        result[i] *= leftProduct;
        leftProduct *= nums[i];
    }

    let rightProduct = 1;
    for (let i = n - 1; i >= 0; i--) {
        result[i] *= rightProduct;
        rightProduct *= nums[i];
    }

    return result;
}
