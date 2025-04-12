function climbStairs(n: number): number {
    // 방법 1: (Failed)
    // Set 객체에 '1', '2'를 담고 while문으로 계속 증가시키면서 계산하는 방법

    // 시간 복잡도: O(n * 2^n) - 각 단계마다 가능한 모든 조합을 생성하므로 지수적으로 증가
    // 공간 복잡도: O(2^n) - 최악의 경우 모든 가능한 조합을 저장해야 함
    // 실패 이유: 시간 초과
    const getResult1 = (): number => {
        const currentSet = new Set<string>(['1', '2']);
        const resultSet = new Set<string>();

        while (currentSet.size > 0) {
            const nextSet = new Set<string>();

            currentSet.forEach((path) => {
                const sum = [...path].reduce((acc, cur) => acc + parseInt(cur), 0);
                if (sum === n) resultSet.add(path);
                else if (sum < n) {
                    nextSet.add(path + '1');
                    nextSet.add(path + '2');
                }
            });

            currentSet.clear();
            nextSet.forEach((v) => currentSet.add(v));
        }

        return resultSet.size;
    };

    // 방법 2:
    // 앞 2가지 더하기 

    // 시간 복잡도: O(n) - n까지 한 번의 반복문만 실행
    // 공간 복잡도: O(1) - 고정된 변수(prev2, prev1)만 사용하여 추가 메모리 사용 없음
    const getResult2 = () => {
        if(n <= 2) {
            return n;
        }
        
        let prev2 = 1;
        let prev1 = 2;
        for(let i = 3; i <= n; i++) {
            const curr = prev2 + prev1;
            prev2 = prev1;
            prev1 = curr;
        }
        return prev1;
    };

    // return getResult1();
    return getResult2();
};
