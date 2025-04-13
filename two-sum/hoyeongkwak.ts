/*
요구사항 : 숫자 배열에서, 2개의 숫자가 더했을 때. target과 같은 숫자가 되는 값을 찾아서 index를 반환
         단, 같은 index의 숫자는 한번만 사용되어야 함
문제풀이 : Map을 선언하여 숫자 배열의 값과 index를 추가
         배열을 순회하면서, target에서 순회중인 index의 숫자와 뺀 값이 Map에 존재하는지 확인하여
         조건에 맞을 경우, 2개의 숫자의 index를 반환
시간복잡도 : O(n)
공간복잡도 : O(n)
*/
function twoSum(nums: number[], target: number): number[] {
    const sumMap = new Map<number, number>()
    nums.forEach((num, idx) => {
        sumMap.set(num, idx)
    })
    for (let i = 0; i < nums.length; i++) {
        const secondNum = target - nums[i]
        if (sumMap.has(secondNum) && sumMap.get(secondNum) != i) {
            return [i, sumMap.get(secondNum)]
        }
    }
    return []
};