/**
 * 세 숫자의 합이 0이 되는 조합 찾기
 * 알고리즘 복잡도:
 * - 시간복잡도: O(n^2)
 * - 공간복잡도: O(1)
 * @param nums
 */
function threeSum(nums: number[]): number[][] {
    // 정렬
    nums.sort((a, b) => a - b)
    let result: number[][] = []

    // 투포인터
    for (let i = 0; i < nums.length - 2; i++) {
        if (i > 0 && nums[i] === nums[i - 1]) continue;

        let start = i + 1
        let end = nums.length - 1
        const target = -nums[i] // 고정 숫자를 이용
        // start + end + target === 0 이므로, start + end === -target

        while (start < end) {
            const sum = nums[start] + nums[end]
            if (sum === target) {
                result.push([nums[i], nums[start], nums[end]])

                // 배열 중복 값 건너뛰기
                while (start < end && nums[start] === nums[start + 1]) start++
                while (start < end && nums[start] === nums[end - 1]) end--

                // 포인터 이동
                start++
                end--
            } else if (sum < target) {
                start++
            } else {
                end--
            }
        }
    }
    return result
}
