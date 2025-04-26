/**
 * @param {string} s
 * @return {number}
 */
var numDecodings = function(s) {
    if (s[0] === '0') return 0;
    
    let count = 0;
    const memo = {};
    
    function backtrack(index, curr) {
        // 기저 조건: 문자열 끝까지 왔으면 유효한 디코딩 발견
        if (index === s.length) {
            count++;
            return;
        }
        
        // 메모이제이션 키 생성
        const key = index;
        if (memo[key] !== undefined) {
            count += memo[key];
            return;
        }
        
        // 이전 카운트 저장
        const prevCount = count;
        
        // Case 1: 한 자리 숫자로 디코딩 (1~9)
        if (s[index] !== '0') {
            const oneDigit = s[index];
            curr.push(oneDigit);
            backtrack(index + 1, curr);
            curr.pop();
        }
        
        // Case 2: 두 자리 숫자로 디코딩 (10~26)
        if (index + 1 < s.length) {
            const twoDigit = s.substring(index, index + 2);
            const num = parseInt(twoDigit);
            if (num >= 10 && num <= 26) {
                curr.push(twoDigit);
                backtrack(index + 2, curr);
                curr.pop();
            }
        }
        
        // 현재 위치에서 발견한 디코딩 방법 수 저장
        memo[key] = count - prevCount;
    }
    
    backtrack(0, []);
    return count;
};
