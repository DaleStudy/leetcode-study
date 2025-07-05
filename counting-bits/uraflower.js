/**
 * 두 번째 풀이
 * 시간복잡도: O(n)
 * 공간복잡도: O(n)
 * @param {number} n
 * @return {number[]}
 */
const countBits = function (n) {
    const arr = [0];

    for (let i = 1; i < n + 1; i++) {
        arr[i] = arr[i >> 1] + (i & 1);
        // i >> 1: 최하위 비트를 제외한 값. 이걸 이용해서 이전 인덱스 사용(dp)
        //         i // 2 (2로 나눈 몫)와 같음.
        // i & 1: 최하위 비트 (1 또는 0)
    }

    return arr;
};

/**
 * 첫 번째 풀이
 * 시간복잡도: O(n * log n)
 * 공간복잡도: O(n)
 * @param {number} n
 * @return {number[]}
 */
const countBits = function (n) {
    const arr = [];

    for (let i = 0; i < n + 1; i++) {
        const bin = i.toString(2); // O(log n)

        let num = 0;
      
        // O(log n)
        for (let char of bin) {
            if (char === '1') num++;
        }

        arr.push(num);
    }

    return arr;
};
