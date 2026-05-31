/**
 * @param nums - 정수 배열
 * @returns - 세 요소를 합해 0이 되는 값의 배열
 * @description
 * - 투 포인터 방식
 * - 결국 유니크한 조합을 찾으며 중복을 제외하는 방향
 * - 무조건 적인 반복 줄이기가 아닌 효율적 범위 반복을 학습해야함
 * - 시간 복잡도 O(N^2)
 * - 공간 복잡도 O(log N)
 */
function threeSum(nums: number[]): number[][] {
  const answer: number[][] = [];
  nums.sort((a, b) => a - b);

  for (let i = 0; i < nums.length - 2; i++) {
    if (i && nums[i] === nums[i - 1]) {
      continue;
    }

    let left = i + 1;
    let right = nums.length - 1;

    while (left < right) {
      const sum = nums[i] + nums[left] + nums[right];

      if (sum === 0) {
        answer.push([nums[i], nums[left], nums[right]]);
        while (left < right && nums[left] === nums[left + 1]) {
          left++;
        }
        while (left < right && nums[right] === nums[right - 1]) {
          right--;
        }
        left++;
        right--;
      } else if (sum < 0) {
        left++;
      } else {
        right--;
      }
    }
  }

  return answer;
}

const nums = [-1, 0, 1, 2, -1, -4];
threeSum(nums);

