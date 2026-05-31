function maxArea(height: number[]): number {
    let result = 0;
    let left = 0;
    let right = height.length - 1;

    // 입력 원소의 갯수가 10만개까지이므로, O(n^2)은 시간초과
    // Two Pointer 활용
    while (left < right) {
        const leftPillar = height[left];
        const rightPillar = height[right];

        // "면적"은 둘의 높이 중 적은 쪽과, 인덱스 차이를 곱한 값
        const area = (right - left) * Math.min(leftPillar, rightPillar);

        result = Math.max(result, area);

        // 투 포인터 이동 기준 - 무엇을 버리고, 무엇을 남길까?
        // 둘 중 높이가 더 낮은 쪽을 버리는 것이 더 많은 면적을 만들기 위한 합리적 선택
        if (leftPillar > rightPillar) {
            right--;
        } else {
            left++;
        }
    }

    return result;
};
