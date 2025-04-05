/**
 * Solution 1. 배열에서 짝 찾기
 *
 * [Idea]
 * 단순하게 nums를 순회하면서 현재 원소(num)과 합해서 target을 만들 수 있는 원소가 있는지 확인함
 *
 * [Time Complexity]
 * O(n^2) (n: nums의 원소 개수)
 * nums를 순회하면서 (O(n)) Array.indexOf 메소드로 짝이 되는 원소를 찾는 방식 (O(n))
 * O(n)이 중첩되어 있으므로 O(n^2)
 *
 * [Space Complexity]
 * O(1)
 */
function twoSum1(nums: number[], target: number): number[] {
  for (let idx = 0; idx < nums.length - 1; idx++) {
    const complementIdx = nums.indexOf(target - nums[idx], idx + 1);
    if (complementIdx !== -1) {
      return [idx, complementIdx];
    }
  }
  // 타입 에러를 제거하기 위해 추가한 코드.
  // 답이 무조건 존재한다는 조건이 있었으므로 이 코드에는 도달하지 않는다.
  return [];
}

/**
 * Solution 2. Map을 이용하기 - 1
 *
 * [Idea]
 * O(n^2)보다 작게 만들 수 있는 방법은 인덱스를 찾는 데 걸리는 시간을 줄이는 것이라 생각해서 검색 시간이 짧은 Map을 활용함.
 *
 * [Time Complexity]
 * O(n) (n: nums의 원소 개수)
 * Map을 생성할 때 O(n)
 * Map에서 짝이 되는 원소를 찾는 것은 O(1)
 *
 * [Space Complexity]
 * O(n) (n: nums의 원소 개수)
 * Map을 생성할 때 필요한 공간 n
 */
function twoSum2(nums: number[], target: number): number[] {
  const numMap = nums.reduce((map, num, idx) => {
    map.set(num, idx);
    return map;
  }, new Map());

  for (let idx = 0; idx < nums.length; idx++) {
    const complementIdx = numMap.get(target - nums[idx]);
    if (complementIdx !== undefined && complementIdx !== idx) {
      return [idx, complementIdx];
    }
  }

  return [];
}

/**
 * Solution 3. Map을 이용하기 - 2
 *
 * [Idea]
 * Map을 미리 생성하지 않고 짝을 찾는 for loop에서 Map을 생성한다.
 * [a, b]가 답일 때 지금까지는 a를 기준으로 b를 찾았지만 지금은 b를 기준으로 a를 찾게 되는 것!
 *
 * [Time Complexity]
 * O(n) (n: nums의 원소 개수)
 *
 * [Space Complexity]
 * O(n) (n: nums의 원소 개수)
 * Solution 1보다 조금 메모리를 덜 쓴다.
 */
function twoSum3(nums: number[], target: number): number[] {
  const numMap = new Map();

  for (let idx = 0; idx < nums.length; idx++) {
    const complementIdx = numMap.get(target - nums[idx]);
    if (complementIdx !== undefined) {
      return [idx, complementIdx];
    }
    numMap.set(nums[idx], idx);
  }

  return [];
}
