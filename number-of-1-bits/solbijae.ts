function hammingWeight(n: number): number {
    // 첫시도: 시간/공간 복잡도 O(log n)
    // const toBinary  = n.toString(2).split('').map(Number);
    // let answer = 0;

    // for (let i=0; i<toBinary.length; i++) {
    //     if (toBinary[i] === 1) answer++;
    // }

    // return answer;

    // 두번째 시도: 시간 복잡도: O(log n), 공간 복잡도: O(1)
    // let count = 0;

    // while(n>0) {
    //     if (n%2 === 1) count++;
    //     n = Math.floor(n/2);
    // }

    // return count;

    // 시간, 공간 복잡도는 두번째와 같지만, 비트 연산이 CPU에서 직접 처리되는 저수준 명령어로 수행되어 연산 비용이 낮기 때문에 산술연산보다 더 빠름
    let count = 0;

    while (n > 0) {
        count += n & 1; // 마지막 비트가 1이면 count++
        n >>>= 1;       // 부호 없는 비트 시프트
    }

    return count;
};
