/**
 * NOTE: 중복이 됨을 판단하여 boolean 값을 반환해야 하는 문제.
 * 중복이 발생했을 경우 빠르게 true 값을 반환, 마지막 값까지 순회할 때도 중복이 없는 경우 false를 반환.
 */
function containsDuplicate1(nums: number[]): boolean {
  let isDuplicate = false;
  let hashMap = new Set();

  for (let i = 0; i < nums.length; i++) {
    if (hashMap.has(nums[i])) {
      // 중복이 발생했을 경우 빠르게 true 값을 반환하고 반복문 종료
      isDuplicate = true;
      break;
    }

    // 중복이 없는 경우 해시맵에 추가
    hashMap.add(nums[i]);
  }

  return isDuplicate;
}

function containsDuplicate2(nums: number[]): boolean {
  return new Set(nums).size !== nums.length;
}

// 두 풀이 전부 시간복잡도 O(n), 공간복잡도 O(n)
