var reverseBits = function(n) {
    let binary = n.toString(2).padStart(32, '0'); // 32비트 보장
    let reversed = binary.split('').reverse().join('');
    return parseInt(reversed, 2); // 이진수로 파싱!
    //padStart(), reverse(), split(), join() 모두 O(N)이 들어가는 작업이기 때문에 아래 코드에 비해서 느릴 수 밖에 없음
};
var reverseBits2 = function(n) {
    let result = 0;
    for (let i = 0; i < 32; i++) {
        result <<= 1;
        result |= n & 1;
        n >>>= 1;
    }
    return result >>> 0;
};
