/**
 * @description nums 배열에서 중복 숫자 확인
 * @param nums - 숫자 배열
 * @returns boolean - 중복 숫자 여부
 */
const containsDuplicate = (nums: number[]) => {
  const hasSeen = new Set<number>();

  for (const num of nums) {
    if (hasSeen.has(num)) {
      return true;
    }
    hasSeen.add(num);
  }
  return false;
};
