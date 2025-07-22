function twoSum(nums: number[], target: number): number[] {
    // 첫 코드: 시간 복잡도가 O(n^2)로 개선 필요
    // for (let i=0; i<nums.length-1; i++) {
    //     for (let j=1; j<nums.length; j++) {
    //         if (nums[i] + nums[j] === target) return [i, j];
    //     }
    // }

    // 시간 공간 모두 O(n)으로 만들기 위해 해시맵 사용
    const map = new Map();
    for (let i=0; i<nums.length; i++) {
        const complement = target - nums[i];
        if (map.get(complement) !== undefined) {
            return [map.get(complement)!, i];
        } else {
            map.set(nums[i], i);
        }
    }
};
