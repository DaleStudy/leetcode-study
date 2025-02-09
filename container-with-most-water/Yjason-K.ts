/**
 * 계산할 수 있는 면적에서 가장 큰 면적 구하기.
 * 
 * @param {number[]} height - x 축 방향의 높이 배열 
 * @returns {number} - 가장 넓은 면적 반환
 * 
 * 시간 복잡도 O(n)
 * - n은 height 배열의 길이
 * 
 * 공간 복잡도 O(1) 
 * - 포인터 및 결과값 저장 공간만 사용
 */
function maxArea(height: number[]): number {
    let start = 0; // 시작 포인터 초기화
    let end = height.length - 1; // 끝 포인터 초기화
    let result = 0; // 최대 면적 저장

    while (start < end) {
        // 현재 면적 계산
        const currentArea = Math.min(height[start], height[end]) * (end - start);
        // 최대 면적 업데이트
        result = Math.max(result, currentArea);

        // 포인터 이동 (높이가 낮은 쪽을 이동)
        if (height[start] > height[end]) {
            end--;
        } else {
            start++;
        }
    }

    return result;
}

