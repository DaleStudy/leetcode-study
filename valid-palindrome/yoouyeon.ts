// [125] Valid Palindrome

/**
 * Solution 1. 문자열 직접 만들어서 비교하기
 *
 * [Idea]
 * 문제에 주어진 조건을 그대로 구현해서 풀었다.
 * 소문자로 변환한 뒤에 Alphanumeric character만 남긴 cleaned 문자열과
 * cleaned 문자열을 뒤집은 reversed 문자열을 만들어서
 * 둘이 비교해서 같으면 팰린드롬, 아니면 팰린드롬이 아니라고 판단했다.
 *
 * [Time Complexity]
 * 문자열을 조건에 맞게 가공하는 과정에서 s의 길이만큼 상수 번 순회하기 때문에 시간 복잡도는 O(n)
 *
 * [Space Complexity]
 * reversed 문자열을 따로 만들어 저장하므로 공간 복잡도는 O(n)
 *
 */
function isPalindrome1(s: string): boolean {
  // replace: 소문자가 아니고 숫자가 아닌 것을 모두 ''으로 치환(제거)한다.
  const cleaned = s.toLowerCase().replace(/[^a-z0-9]/g, "");
  // string에는 reverse 내장함수가 없으므로, string -> array -> reverse -> string (join) 과정으로 뒤집는다.
  const reversed = cleaned.split("").reverse().join("");

  return cleaned === reversed;
}

/**
 * Solution 2. 포인터를 활용하기
 * [Idea]
 * 문자열을 가공하는 데 필요한 추가적인 순회 시간을 줄이고 reversed를 따로 저장하지 않아도 되는 방법
 * s의 왼쪽, 오른쪽을 순서대로 비교하면서 아래와 같은 과정을 거친다.
 * 1. 알파벳(소문자로 변환하지 않았으므로 대소문자 모두) 또는 숫자가 아닌 경우를 제외한다 (포인터 이동)
 * 2. 현재 포인터가 가리키는 두 알파벳이 소문자로 변환했을 때 같지 않으면 팰린드롬이 아니다.
 * 3. 알파벳이 같다면 다음 문자를 비교하기 위해 포인터를 옮긴다.
 *
 * [Time Complexity]
 * Solution 1과 동일하게 O(n)이지만 s를 1번만 순회한다
 *
 * [Space Complexity]
 * left, right 포인터를 저장할 상수 크기의 메모리가 필요하므로 공간 복잡도는 O(1)이다.
 */
function isPalindrome2(s: string): boolean {
  let left = 0,
    right = s.length - 1;

  while (left < right) {
    while (left < right && s[left].match(/[^A-Za-z0-9]/)) {
      left++;
    }
    while (left < right && s[right].match(/[^A-Za-z0-9]/)) {
      right--;
    }
    if (s[left].toLowerCase() !== s[right].toLowerCase()) {
      return false;
    }
    left++;
    right--;
  }

  return true;
}
