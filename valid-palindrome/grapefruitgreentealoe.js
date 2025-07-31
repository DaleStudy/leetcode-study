/**
 * @param {string} s
 * @return {boolean}
 */

String.prototype.isAlphaNum = function() {
  return /^[a-z0-9]$/i.test(this);
};
var isPalindrome = function(s) {
    //chatAt의 범위의 string, number만 건진다
    const ss = s.split('').filter((x)=>x.isAlphaNum()).map(x=>x.toLowerCase())
    //그 다음엔 index를 양쪽에서 비교하기
    for(let i=0;i<(ss.length/2);i++){
        console.log(ss[i],ss[ss.length-1-i])
        if(ss[i]!==ss[ss.length-1-i]) return false
    }
    return true
};

// 시간 복잡도 O(N)
// 공간 복잡도 O(N)

//2. 투포인터 방식으로, 필터링과 string 메서드를 그때마다 사용하는 방식으로 효율성 올리기
var isPalindrome = function(s) {
    let left = 0;
    let right = s.length - 1;
    //각 포인터가 영숫자 문자를 만날 때까지 이동
    while (left < right) {
        while (left < right && !s[left].isAlphaNum()) {
            left++;
        }
        while (left < right && !s[right].isAlphaNum()) {
            right--;
        }
        if (left < right && s[left].toLowerCase() !== s[right].toLowerCase()) {
            return false;
        }
        left++;
        right--;
    }

    return true;
};

// 시간 복잡도 O(N)
// 공간 복잡도 O(1)

/*
더 효율적이게 푸는 방법
1. String.prototype 확장 지양
성능적인 측면에서 String.prototype 메서드 호출이 직접적인 헬퍼 함수 호출보다 아주 미세하게 오버헤드가 있을 수 있다 (실제로는 거의 무시할 수 있는 수준)

2. isAlphaNum 내부 로직 최적화 (Micro-optimization)
- 정규 표현식 엔진이 내부적으로 파싱되고 컴파일되는 오버헤드가 있기 때문에, 정규 표현식, 단순한 문자 범위 체크에는 문자 코드(char code) 비교가 더 빠를 수 있다.

*/