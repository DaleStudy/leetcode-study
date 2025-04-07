/**
 * [Problem]: [001] Two Sum
 * (https://leetcode.com/problems/two-sum/description/)
 */

function twoSum(nums: number[], target: number): number[] {
    // 시간 복잡도 O(n^2)
    // 공간 복잡도 O(1)
    function doubleLoopFunc(num: number[], target: number): number[] {
        for (let i = 0; i < nums.length; i++) {
            for (let j = i + 1; j < nums.length; j++) {
                if (nums[i] + nums[j] === target) return [i, j];
            }
        }

        return [];
    }

    // 시간 복잡도 O(n)
    // 공간 복잡도 O(n)
    function differenceMap(nums: number[], target: number): number[] {
        const diffMap = new Map<number, number>();

        for (let [i, num] of nums.entries()) {
            const diff = target - num;
            if (diffMap.has(diff)) return [i, diffMap.get(diff)!];
            diffMap.set(num, i);
        }

        return [];
    }

    // 시간 복잡도 O(nlog n) - sort
    // 공간 복잡도 O(1)
    // 정렬을 통해 인덱스 값을 유지할 수 없어서 실패
    // 인덱스 값이 아닌 배열의 요소를 반환하는 문제에서는 사용이 가능할 듯?
    function twoPointerFunc(nums: number[], target: number): number[] {
        nums.sort((a, b) => a - b);
        let leftPointer = 0;
        let rightPointer = nums.length - 1;

        while (leftPointer < rightPointer) {
            const twoSum = nums[leftPointer] + nums[rightPointer];
            if (twoSum === target) return [leftPointer, rightPointer];

            if (twoSum < target) leftPointer++;
            if (twoSum > target) rightPointer--;
        }

        return [];
    }

    return twoPointerFunc(nums, target);
}

console.log(twoSum([2, 7, 11, 15], 9));
