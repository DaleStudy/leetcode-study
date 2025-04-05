/**
 * Solution 1. Set을 활용하기 1
 *
 * [Idea]
 * nums에서 중복된 원소를 제거하기 위해서 nums를 이용해서 중복을 허용하지 않는 자료구조인 Set을 생성 (numSet)
 * 중복된 원소가 있었다면 set을 생성할 때 제거되어 nums의 길이와 numSet의 크기가 다를 것이므로 비교해서 결과를 반환
 *
 * [Time Complexity]
 * O(n) (n: nums의 원소 개수)
 * nums 배열을 이용해서 Set을 만드는 것에서 O(n)
 *
 * [Space Complexity]
 * O(n) (n: nums의 원소 개수)
 * numSet을 생성하기 위해 최대 n만큼의 공간이 추가로 필요함
 */
function containsDuplicate1(nums: number[]): boolean {
  const numsSet = new Set<number>(nums);
  return numsSet.size !== nums.length;
}

/**
 * Solution 2. Set을 활용하기 2
 *
 * [Idea]
 * 최악의 경우가 아닐 때 약간 더 빠르게 결과를 반환할 수 있는 방법
 * 중복인 원소를 마주하자마자 바로 반환하기 때문에 아주 조금 더 빠름
 *
 * [Time Complexity]
 * O(n) (n: nums의 원소 개수)
 *
 * [Space Complexity]
 * O(n) (n: nums의 원소 개수)
 * 생성자로 추가하는 것과 add로 추가하는 차이 때문인지 실제로 사용된 메모리는 Solution 1보다 조금 많다.
 */
function containsDuplicate2(nums: number[]): boolean {
  const numSet = new Set<number>();

  for (const num of nums) {
    if (numSet.has(num)) {
      return true;
    }
    numSet.add(num);
  }

  return false;
}
