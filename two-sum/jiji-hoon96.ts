/**
 * 두 수의 합이 특정 값(target)이 되게 하는 나머지 하나의 수를 찾는 문제 => 보수를 찾는 문제
 * @param nums - 정수 배열
 * @param target - 두 수의 합
 * @returns 두 수의 인덱스
 *
 * 풀이 1
 * 이중 for 문을 사용해 nums의 요소를 더한 값이 target과 같은지 확인한다.
 * 이렇게 해결했더니 O(n^2)의 시간복잡도로 시간초과가 발생할 수 있다고 판단.
 *
 * 풀이 2
 * Map을 사용해 for 문을 한 번만 사용하도록 수정해보았다.
 */

function twoSum(nums: number[], target: number): number[] {
    const newMap = new Map<number,number>();

    for(let i=0; i<nums.length; i++){
        const complement = target - nums[i];

        if(newMap.has(complement)){
            return [newMap.get(complement)!, i]
        }

        newMap.set(nums[i], i)
    }
};
