function rob(nums: number[]): number {
    // 시간 초과를 막기 위해 Memo 객체 추가
    const memo: Record<number, number> = {};
    
    function dfs (start: number): number {
        // memo에 저장된 값 있으면 사용
        if(memo[start] != null) {
            return memo[start];
        }

        // 배열 벗어난 인덱스 접근이면 0리턴
        if(start >= nums.length) {
            return 0;
        }

        // 현재 요소의 값과 하나 건너뛴 요소의 기대값 / 다음 요소의 기대값 중 더 큰 값을 사용
        memo[start] = Math.max(nums[start] + dfs(start + 2), dfs(start + 1));
        return memo[start];
    }

    return dfs(0);
};
