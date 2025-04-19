function hammingWeight(n: number): number {

    // 풀이 1:
    // binary로 변환 후 1 count
    // 시간 복잡도: O(log n) 
    // 공간 복잡도: O(log n) 
    const getResult1 = () => {
        const binaryNum = n.toString(2);

        let count = 0;

        for(let i = 0; i < binaryNum.length; i++) {
            if(binaryNum.charAt(i) === '1') {
                count++
            }
        }

        return count;
    };

    // 풀이 2:
    // 비트 연산을 활용할 수 있다고 함 (From GPT)
    // 시간 복잡도: O(log n) 
    // 공간 복잡도: O(1) 
    // const getResult2 = () => {
    //     let count = 0;

    //     while (n !== 0) {
    //         count += n & 1;  
    //         n >>>= 1; 
    //     }

    //     return count;
    // }

    return getResult1();
    // return getResult2();
};
