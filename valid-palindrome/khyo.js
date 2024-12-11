// 풀이
// 1. 영어, 숫자만 남기고 소문자로 변환한 newStr 생성
// 2. 투포인터를 이용해 문자열 팰린드롬 여부 확인 (초기값 : true)
// 3. 중간에 팰린드롬이 아닌 지점을 발견하면 flag를 false로 변경 후 return

// TC : O(N)
// SC : O(N)

var isPalindrome = function(s) {
  const newStr = s.replace(/[^a-zA-Z0-9]/g, '').toLowerCase();
  let flag = true
  let left = 0, right = newStr.length - 1
  while(left < right){
      if(newStr[left] === newStr[right]) {
          left += 1;
          right -= 1;
      }else {
          flag = false;
          break;
      }
  }
  return flag
};
