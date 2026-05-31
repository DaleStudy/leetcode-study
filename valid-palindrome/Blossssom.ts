/**
 * @param s - 입력 문자열
 * @returns - 입력 문자열이 palindrome 인지 반환
 * @description
 * 풀이 1 - 시간복잡도: O(n), 공간복잡도: O(n)
 * 풀이 2 - 시간복잡도: O(n), 공간복잡도: O(1) - 초반 정규식 스캔 및 소문자 변경이 한번에 일어나지 않고, 조기 종료
 * 풀이 3 - 1번과 복잡도는 같지만 split으로 실제 실행시간은 훨씬 빠르게 진행
 */
// function isPalindrome(s: string): boolean {
//   const clearString = s.replace(/[^a-zA-Z0-9]/g, "").toLocaleLowerCase();
//   let strLen = clearString.length - 1;
//   if (!clearString.length) {
//     return true;
//   }

//   for (let i = 0; i < Math.floor(clearString.length / 2); i++) {
//     if (clearString[i] !== clearString[strLen]) {
//       return false;
//     }
//     strLen--;
//   }
//   return true;
// }

// function isPalindrome(s: string): boolean {
//   let i = 0;
//   let j = s.length - 1;

//   while (i < j) {
//     if (!isAlphaNum[s[i]]) {
//       i++;
//       continue;
//     }

//     if (!isAlphaNum[s[j]]) {
//       j--;
//       continue;
//     }

//     if (s[i].toLocaleLowerCase() !== s[j].toLocaleLowerCase()) {
//       return false;
//     }

//     i++;
//     j--;
//   }
//   return true;
// }

// function isAlphaNum(str: string): boolean {
//   const charC = str.charCodeAt(0);
//   return (
//     (charC >= "0".charCodeAt(0) && charC <= "9".charCodeAt(0)) ||
//     (charC >= "A".charCodeAt(0) && charC <= "Z".charCodeAt(0)) ||
//     (charC >= "a".charCodeAt(0) && charC <= "z".charCodeAt(0))
//   );
// }

function isPalindrome(s: string): boolean {
  const cleaned = s
    .toLowerCase()
    .replace(/[^a-zA-Z0-9]/g, "")
    .split("");
  let left = 0;
  let right = cleaned.length - 1;
  while (left < right) {
    if (cleaned[left] === cleaned[right]) {
      left++;
      right--;
    } else {
      return false;
    }
  }
  return true;
}


