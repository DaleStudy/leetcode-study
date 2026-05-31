/*
nums를 순회하며 최대 sum을 찾는다. 다음 규칙을 따른다
- 매 순간 숫자를 더해 가며 현재까지의 합과 최대합 비교, 갱신
- 만약 해당 인덱스 num을 더했을 때 0보다 작아지면 현재까지의 값을 0으로 초기화(총합 버림)

*/

function maxSubArray(nums: number[]): number {
    let result = -Infinity;
    let curSum = 0;

    for (let num of nums) {
        curSum += num;
        result = Math.max(result, curSum);
        if (curSum < 0) curSum = 0;
    }

    return result;
}
