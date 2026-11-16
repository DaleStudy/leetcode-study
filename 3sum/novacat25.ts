/* 
시간 복잡도(TC): O(n^2)
공간 복잡도(SC): O(1)
풀이: 배열을 정렬하여 Two Pointer 기법을 사용할 수 있게 세팅한 후, 3개의 포인터를 이용하여 합이 0이 되는 조합을 찾는다. 중복된 조합은 제외한다.
기타: 해당 문제는 처음 접하는 유형이므로, 추후 보충 학습이 필요함.
*/
const threeSum = (nums: number[]): number[][] => {
  const SUM_TARGET = 0
  const res: number[][] = []
  const n = nums.length

  nums.sort((a, b) => a - b)

  for (let i = 0; i < n - 2; i++) {
    // -1, -2 index out of bounds check
    if (i > 0 && nums[i] === nums[i - 1]) continue

    let j = i + 1
    let k = n - 1

    while (j < k) {
      const sum = nums[i] + nums[j] + nums[k]

      if (sum === SUM_TARGET) {
        res.push([nums[i], nums[j], nums[k]])

        j++
        k--

        // 중복값 제외
        while (j < k && nums[j] === nums[j - 1]) j++
        while (j < k && nums[k] === nums[k + 1]) k--
      } else if (sum < SUM_TARGET) j++
      else k--
    }
  }

  return res
}
