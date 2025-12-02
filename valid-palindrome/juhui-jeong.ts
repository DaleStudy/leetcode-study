// 시간 복잡도: O(n)
// 공간 복잡도: O(n)
function isPalindrome(s: string): boolean {
  //1. s에서 문자와 숫자가 아닌 다른 것들은 제거
  //2. 대문자 -> 소문자, 띄어쓰기, 공백 제거
  let originalString = s;
  let alphabeticString = originalString.replace(/[^a-zA-Z0-9]/g, '');
  const filteredString = alphabeticString.toLowerCase().trim();

  //3. 제거 후 length === 0 일 경우 true로 결과 값 반환.
  if (filteredString.length === 0) {
    return true;
  }

  let count = 0;
  let roundedStringLength = Math.round(filteredString.length / 2);
  for (let i = 0; i < roundedStringLength; i++) {
    // 양 끝의 글자가 동일한지 체크하고
    if (filteredString[i] === filteredString[filteredString.length - i - 1]) {
      count += 1;
    }
  }
  return count === roundedStringLength ? true : false;
}
