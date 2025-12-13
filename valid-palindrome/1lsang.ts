function isPalindrome(s: string): boolean {
  // console.log('A'.charCodeAt(0), 'Z'.charCodeAt(0)); // 65 90
  // console.log('a'.charCodeAt(0), 'z'.charCodeAt(0)); // 97 122
  // console.log('0'.charCodeAt(0), '9'.charCodeAt(0)); // 48 57

  // 문자열 변환 과정
  let converted = ''
  for (let c of s) {
    const charCode = c.charCodeAt(0);
    if (charCode >= 65 && charCode <= 90) {
      converted += c.toLowerCase();
    }
    else if ((charCode >= 97 && charCode <= 122) || (charCode >= 48 && charCode <= 57)) {
      converted += c;
    }
  }
  
  // palindrome 판단 조건
  const length = converted.length;
  
  for (let i = 0; i < length/2; i ++) {
    if (converted[i] !== converted[length - 1 - i]) return false;
  }

  return true;  
};
