/**
 * 시간 복잡도: 상수(32)번 반복이 일어나므로 O(1)
 * 공간 복잡도: 상수(32) 크기의 배열을 생성하므로 O(1)
 */
/**
 * @param {number} n - a positive integer
 * @return {number} - a positive integer
 */
var reverseBits = function(n) {
    let i = 0;
    let arr = [];
    while(i < 32) {
        arr.push(n % 2);
        n = Math.floor(n / 2);
        i++;
    }
    const bi = arr.reverse().join('');
    const reversedBi = bi.split('').reverse().join('');
    return parseInt(reversedBi, 2);
};
