/**
 * 하나 이상 건너 뛴 값을 더한 것중 가장 높은 값의 합을 구하기
 * @param nums
 */
function rob(nums: number[]): number {

    if(nums.length === 1) return nums[0];

    // 0 + 2 ...
    // 1 + 3 ...
    // Max(인덱스 0부터 더한 것, 인덱스 1부터 더한 것)

    // 접근 (1) - 양 옆의 값을 제외하고 홀수/짝수 인덱스 값들을 더했음
    // [2, 1, 1, 2] 일 때, 답이 4가 나와야 함
    // let max = 0
    // let odd = 0
    // let even = 0
    // for(let i = 0; i < nums.length; i++) {
    //     if(i % 2 == 0) {
    //         console.log(nums[i], 'even >>>', even);
    //         even += nums[i];
    //     } else {
    //         console.log(nums[i], 'odd >>>', odd);
    //         odd += nums[i];
    //     }
    // }
    // console.log(even, '===', odd);
    // max = Math.max(even, odd);

    // 접근 (2) - max 값을 저장해두고 Math.max(하나 이상 건너뛴 값 + 현재 값 더한 것, max) 를 구함
    let prev = 0
    let max = 0
    let temp = 0
    for(let i = 0; i < nums.length; i++) {
        temp = max
        max = Math.max(prev + nums[i], max) // 이전의 값과 하나 이상 건너뛰고 더한 값 중 최대 값을 구함
        prev = temp

        // console.log(temp, " - ", max, " - ", prev)
    };
    // console.log(max);
    return max;
};
