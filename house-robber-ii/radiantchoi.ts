function rob(nums: number[]): number {
    if (nums.length < 3) {
        return Math.max(...nums);
    }

    // House Robber II의 핵심: 원형으로 연결된 집들을, 연결되지 않은 두 부분으로 나눈다
    let first = nums.slice(0, nums.length - 1);
    let second = nums.slice(1, nums.length);

    // House Robber 점화식의 첫 번째 항: 첫 번째 집과 두 번째 집을, 둘 중 더 큰 값으로 미리 동기화해 둔다
    first[1] = Math.max(first[0], first[1]);
    second[1] = Math.max(second[0], second[1]);

    // 배열 길이 조건을 만족할 경우, House Robber 1번 문제처럼 점화식을 사용하여 각 배열의 값을 업데이트
    if (nums.length > 2) {
        for (let i = 2; i < nums.length - 1; i++) {
            first[i] = Math.max(first[i] + first[i - 2], first[i - 1])
            second[i] = Math.max(second[i] + second[i - 2], second[i - 1])
        }
    }

    // 두 결과 중 더 큰 것을 반환
    let firstResult = Math.max(...first);
    let secondResult = Math.max(...second);

    return Math.max(firstResult, secondResult);
};
