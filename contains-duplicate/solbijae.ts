function containsDuplicate(nums: number[]): boolean {
    const set = new Set(nums);
    const setSize = set.size;
    const numsLength = nums.length;

    return setSize !== numsLength ? true : false;

    // Big O
    // 시간 복잡도: O(n) 한번씩 순회하면서 확인
    // 공간 복잡도: O(n) Set을 사용해 배열 크기만큼 메모리가 더 사용됨
};
