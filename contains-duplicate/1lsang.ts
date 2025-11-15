function containsDuplicate(nums: number[]): boolean {
    // Javascript의 Set은 내부적으로 해시테이블을 이용해서, O(n)으로 중복 제거
    const uniqueNums = Array.from(new Set(nums).values());
    return uniqueNums.length !== nums.length;
};
