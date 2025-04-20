/**
 * @param {number} n
 * @return {number}
 */
var hammingWeight = function(n) {
    function recursive(num) {
        // 종료조건
        if(String(num) === '1') {
            return '1'
        }
        // 재귀호출
        const q = Math.floor(num / 2) // 몫
        const r = num % 2 // 나머지
        const total = r + recursive(q)

        // 데이터 통합
        return total
    }
    const binaryString = recursive(n)
    const result = [...binaryString].map(Number).reduce((a,b) => a + b, 0)
    
    return result
};
