/**
 * Set 자료구조를 사용하여 중복 확인 (시간 복잡도: O(n) )
 * @param nums 중복 검사할 숫자 배열
 * @returns boolean 중복 여부
 */

function containsDuplicate(nums: number[]): boolean {
    let unique: Set<number> = new Set([]);
    for (const num of nums) {
        if (unique.has(num)) {
            return true
        } else {
            unique.add(num)
        }
    }
    return false;
};
