/**
 * 세 수의 합이 0이 되는 모든 고유한 조합을 찾는 함수
 * 
 * @param {number[]} nums - 정수 배열
 * @returns {number[][]} - 세 수의 합이 0이 되는 조합 배열
 * 
 * 1. 입력 배열 `nums`를 오름차순으로 정렬.
 * 2. 이중 반복문을 사용하여 각 요소를 기준으로 `투 포인터(two-pointer)`를 이용해 조합을 탐색.
 * 3. 중복 조합을 방지하기 위해 `Set`을 사용하여 결과 조합의 문자열을 저장.
 * 4. 조건에 맞는 조합을 `result` 배열에 추가합니다.
 * 
 * 시간 복잡도:
 * - 정렬: O(n log n)
 * - 이중 반복문 및 투 포인터: O(n^2)
 * - 전체 시간 복잡도: O(n^2)
 * 
 * 공간 복잡도:
 * - `Set` 및 `result` 배열에 저장되는 고유 조합: O(k), k는 고유한 조합의 수
 * - 전체 공간 복잡도: O(n + k)
 */
function threeSum(nums: number[]): number[][] {
    const sumSet = new Set<string>();
    const result: number[][] = [];
    nums.sort((a, b) => a - b);

    // 첫 번째 요소를 기준으로 반복문 수행
    for (let i = 0; i < nums.length - 2; i++) {
        // 정렬 된 상태이기 때문에 시작점을 기준으로 다음 값 중복 비교
        if (i > 0 && nums[i] === nums[i - 1]) continue;

        let start = i + 1, end = nums.length - 1;
        while (start < end) {
            const sum = nums[i] + nums[start] + nums[end];
            if (sum > 0) {
                end--;
            } else if (sum < 0) {
                start++;
            } else {
                const triplet = [nums[i], nums[start], nums[end]];
                const key = triplet.toString();
                if (!sumSet.has(key)) {
                    sumSet.add(key);
                    result.push(triplet);
                }
                start++;
                end--;
            }
        }
    }

    return result;
}