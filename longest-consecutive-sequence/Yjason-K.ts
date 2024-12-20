/**
 * 주어진 배열에서 가장 긴 연속된 숫자 시퀀스의 길이를 반환하는 함수
 * - 시간 복잡도: O(n)
 *   - O(n): Set에 숫자를 추가하고, 각 숫자를 순회하면서 연속된 시퀀스를 계산
 * - 공간 복잡도: O(n)
 *   - O(n): 숫자를 저장하기 위한 Set 사용
 * 
 * @param {number[]} nums - 정수 배열
 * @returns {number} - 가장 긴 연속된 숫자 시퀀스의 길이
 */
function longestConsecutive(nums: number[]): number {
    if (nums.length === 0) return 0; // 빈 배열 처리 (길이 0 반환)

    // 1. 배열을 Set에 저장하여 중복을 제거하고 빠른 조회를 가능하게 함 O(n)
    const numSet = new Set(nums);

    let longestSeq = 0; // 가장 긴 연속 시퀀스 길이를 저장할 변수

    // 2. 각 숫자가 시퀀스의 시작점인지 확인
    for (const num of numSet) {
        // 숫자 `num`이 시퀀스의 시작점인지 확인
        // (num-1이 Set에 없다면 num은 시퀀스의 시작점)
        if (!numSet.has(num - 1)) {
            // 새로운 시퀀스 시작
            let curNum = num;
            let curSeq = 1;

            // 3. 시퀀스가 끝날 때까지 길이를 계산 O(n)
            while (numSet.has(curNum + 1)) {
                curNum += 1; // 현재 숫자를 1 증가
                curSeq += 1; // 시퀀스 길이를 1 증가
            }

            // 4. 가장 긴 시퀀스 길이를 업데이트
            longestSeq = Math.max(longestSeq, curSeq);
        }
    }

    return longestSeq; // 가장 긴 연속 시퀀스의 길이 반환
}

