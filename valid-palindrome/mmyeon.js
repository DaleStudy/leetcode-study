/**
 *
 * 접근 방법 :
 *  - 문자열 순회하면서 소문자로 변경한 뒤, 정규식을 이용해 알파벳과 숫자만 추출
 *  - 추출된 문자에 투 포인터 사용해서 앞뒤 문자 같은지 비교.
 *  - 다르면 false 바로 리턴하고, 끝까지 같으면 true 반환
 *
 * 시간복잡도 :
 *  - 문자열 길이가 n일 때, O(n)
 *  - match로 문자열 체크 : O(n)
 *  - 투 포인터로 앞뒤 문자 비교 : O(n)
 *
 * 공간복잡도 :
 *  - 최악의 경우 모든 문자가 알파벳이거나 숫자인 경우 길이가 n이 됨 : O(n)
 *
 * 배운 점 :
 *  - 문자값 필요한 게 아니니까 불필요한 배열 변환(reverse) 줄이기
 *  - 문자열이 조건 범위에 부합하는지 체크할 때는 정규식 활용하기
 */

/**
 * @param {string} s
 * @return {boolean}
 */

var isPalindrome = function (s) {
  const alphanumericCharacters = s.toLowerCase().match(/[a-z0-9]/g) || [];

  let leftPointer = 0;
  let rightPointer = alphanumericCharacters.length - 1;

  while (leftPointer < rightPointer) {
    if (
      alphanumericCharacters[leftPointer] !==
      alphanumericCharacters[rightPointer]
    ) {
      return false;
    }

    leftPointer++;
    rightPointer--;
  }

  return true;
};
