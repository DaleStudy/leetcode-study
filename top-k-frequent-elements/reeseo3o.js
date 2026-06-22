const topKFrequent = (nums, k) => {
    // 1: 등장 횟수 세기
    const countMap = new Map();
    for (const num of nums) {
        countMap.set(num, (countMap.get(num) ?? 0) + 1);
    }

    // 2: 버킷 배열 만들기
    // 인덱스 = 빈도수, 값 = 그 빈도수를 가진 숫자들의 배열
    // 최대 빈도는 nums.length이므로 크기를 nums.length + 1로 설정
    const bucket = Array.from({ length: nums.length + 1 }, () => []);

    for (const [num, freq] of countMap.entries()) {
        bucket[freq].push(num);
    }

    // 3: 뒤(높은 빈도)에서부터 탐색하며 k개 수집
    const result = [];
    for (let i = bucket.length - 1; i >= 0 && result.length < k; i--) {
        for (const num of bucket[i]) {
            result.push(num);
            if (result.length === k) break;
        }
    }

    return result;
}
