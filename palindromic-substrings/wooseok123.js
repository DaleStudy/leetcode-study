var countSubstrings = function (s) {
  let result = 0;
  // 개수를 키워나가며, 각 자리가 대칭을 이루는지 검사한다.

  // substring의 개수 설정
  for (let i = 0; i < s.length; i++) {
    // 시작점 설정
    for (let j = 0; j < s.length - i; j++) {
      let isPalindromic = true;
      // 대칭되는 요소를 하나씩 비교
      for (let k = j; k < Math.ceil((j * 2 + i) / 2); k++) {
        if (s[k] !== s[j * 2 + i - k]) {
          isPalindromic = false;
          break;
        }
      }
      if (isPalindromic) result += 1;
    }
  }

  return result;
};

// TC : o(n^3) | SC : o(1)
