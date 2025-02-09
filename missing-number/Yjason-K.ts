/**
 * 0부터 n까지의 숫자 중 배열에서 누락된 숫자를 찾는 함수
 * @param {number[]} nums - 0부터 n까지의 숫자가 포함된 배열 (순서는 무작위이며 일부 숫자가 누락될 수 있음)
 * @returns {number} - 배열에서 누락된 숫자
 * 
 * 시간 복잡도: O(n)
 *  - Set은 Hash Table로 구현되어 has 메서드가 Array.includes 메서드보다 유리
 *  - Set을 생성하는 데 O(n) 시간이 소요
 *  - 배열 길이만큼 반복문을 돌면서 Set의 존재 여부를 확인하는 데 O(1) * n = O(n)
 *  - 결과적으로 O(n) + O(n) = O(n)
 * 
 * 공간 복잡도: O(n)
 *  - Set 자료구조를 사용하여 입력 배열의 모든 요소를 저장하므로 O(n)의 추가 메모리 사용
 */
function missingNumber(nums: number[]): number {
    // 배열의 숫자를 모두 Set에 추가하여 중복 제거
    const distinctSet = new Set([...nums]);

    // 0부터 n까지의 숫자 중에서 누락된 숫자를 탐색
    for (let i = 0; i < nums.length; i++) {
        // Set에 i가 존재하지 않으면 i가 누락된 숫자
        if (!distinctSet.has(i)) {
            return i;
        }
    }

    // 모든 숫자가 Set에 존재하면 n이 누락된 숫자
    return nums.length;
}
