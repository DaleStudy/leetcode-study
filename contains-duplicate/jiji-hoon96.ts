/**
 * 배열에 중복된 요소가 있는지 확인하는 함수
 * @param nums - 확인할 정수 배열
 * @returns 중복된 요소가 있으면 true, 모든 요소가 고유하면 false
 *
 * 기존에 for문을 사용해 filter,indexOf 방식을 사용했지만, 시간복잡도가 O(n^2)이라서 시간초과가 발생했다.
 * Set을 사용하면 중복된 요소를 제거하고, size를 통해 중복된 요소가 있는지 확인할 수 있다.
 */
function containsDuplicate(nums: number[]): boolean {
    return new Set(nums).size !== nums.length
};
