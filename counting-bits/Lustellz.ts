// Runtime: 6mx
// Memory: 61.10MB

function countBits(n: number): number[] {
    let answer: number[] = Array(n + 1).fill(0);

    for(let i = 1 ; i <= n ; i++){
        let tmp = i;
        while (tmp > 0){
            answer[i] += tmp % 2
            tmp = Math.floor(tmp / 2)
        }
    }

    return answer;
};
