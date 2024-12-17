/**
 * 배열에서 각 숫자의 빈도를 계산한 후 상위 k개의 빈도 요소를 반환하는 함수
 * - 시간 복잡도: O(n + m log m)
 *   - O(n): 숫자 빈도를 계산하는 루프
 *   - O(m log m): 고유 숫자(m)에 대한 정렬
 * - 공간 복잡도: O(m)
 *   - 고유 숫자(m)에 비례한 Map과 정렬된 배열 사용
 * 
 * @param {number[]} nums - 숫자 배열
 * @param {number} k - 반환할 상위 빈도 요소의 개수
 * @returns {number[]} 상위 k개의 빈도 요소 (순서는 상관 없음)
 */
function topKFrequent(nums: number[], k: number): number[] {
    let numMap = new Map(); // 숫자의 빈도를 저장할 Map

    // 1. 숫자 빈도 Map 생성 O(n)
    for (const num of nums) {
        // Map에 현재 숫자가 없으면 1로 초기화, 있으면 1 증가
        const value = numMap.get(num) ? numMap.get(num) + 1 : 1;
        numMap.set(num, value);
    }

    // 2. Map을 [숫자, 빈도수] 배열로 변환한 뒤 빈도수 기준 내림차순 정렬 O(m log m)
    const sortedFrequent = [...numMap.entries()] // Map을 배열로 변환
        .sort((a, b) => b[1] - a[1]) // 빈도수 기준 내림차순 정렬

        // 3. 상위 k개의 숫자만 추출 O(k)
        .slice(0, k)

        // 4. 숫자(key)만 추출 O(k)
        .map(entry => entry[0]);

    return sortedFrequent;
}


