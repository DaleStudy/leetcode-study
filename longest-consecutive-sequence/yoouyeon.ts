/**
 * [Idea]
 * O(n)이기 때문에 정렬 방식은 불가능하다고 판단함. => 특별한 방법이 생각이 안나서 일일이 구간을 확인해 주는 방식을 시도했다.
 * 배열을 순회할 때 빠르게 원소를 찾아야 하기 때문에 Set을 이용하기로 함.
 *
 * [Time Complexity]
 * O(n + n) => O(n)
 * - Set 생성: O(n)
 * - for loop: O(n)
 *   for loop 내부에 while loop가 있긴 하지만 "증가하는 구간의 시작점일 때만 실행되기 때문에" (이걸 놓쳐서 시간 초과 났었다..)
 *   각 원소에 접근하는 횟수는 결국 1번뿐.
 *
 * [Space Complexity]
 * O(n)
 * Set을 생성하기 위해 추가로 필요한 공간
 */

function longestConsecutive(nums: number[]): number {
  const numSet = new Set<number>(nums);
  let longest = 0;

  for (const startNum of numSet) {
    // 증가하는 구간의 시작점인 경우에만 검사한다. (같은 구간을 중복해서 탐색하는 것을 막기)
    // nums.length가 10000인 경우에 뜬 Time Limit Exceeded를 해결하기 위해 추가함...
    if (numSet.has(startNum - 1)) {
      continue;
    }
    let length = 1;
    let currNum = startNum + 1;
    while (numSet.has(currNum)) {
      length++;
      currNum++;
    }
    longest = Math.max(longest, length);
  }

  return longest;
}
