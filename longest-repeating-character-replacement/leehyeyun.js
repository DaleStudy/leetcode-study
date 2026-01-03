/**
 * @param {string} s
 * @param {number} k
 * @return {number}
 */
/*
문제 설명:
주어진 문자열 s와 정수 k가 주어진다.

문자열 s는 대문자 영어 알파벳(A~Z)으로만 구성되어 있으며,
문자열의 길이는 최대 100,000이다.

하나의 연산에서는 문자열 s의 임의의 문자 하나를 선택하여
다른 어떤 대문자 알파벳 문자로든 변경할 수 있다.
이 연산은 최대 k번까지 수행할 수 있다.

목표는 연산을 최대 k번까지 수행한 후,
모든 문자가 동일한 가장 긴 연속 부분 문자열(substring)의 길이를 구하는 것이다.

여기서 부분 문자열은 반드시 연속된 문자들로 이루어져야 하며,
문자열의 일부를 건너뛸 수는 없다.

입력:
- s: 대문자 영어 알파벳으로 이루어진 문자열
- k: 수행 가능한 최대 문자 변경 횟수
- 1 ≤ s.length ≤ 100,000
- 0 ≤ k ≤ s.length

출력:
- 최대 k번의 문자 변경을 통해 만들 수 있는
  모든 문자가 같은 가장 긴 연속 부분 문자열의 길이

예시 1:
입력:
  s = "ABAB", k = 2
설명:
  두 문자를 변경하여 "AAAA" 또는 "BBBB"로 만들 수 있다.
출력:
  4

예시 2:
입력:
  s = "AABABBA", k = 1
설명:
  한 문자를 변경하여 연속된 "BBBB" 부분 문자열을 만들 수 있다.
출력:
  4

주의 사항:
- 변경은 반드시 최대 k번까지만 가능하다.
- 최종적으로 선택한 부분 문자열은
  모든 문자가 동일해야 한다.
*/

var characterReplacement = function(s, k) {
    let left = 0;
    let maxLen = 0;
    let count = {};
    let maxCount = 0;

    for (let right = 0; right < s.length; right++)
    {
        const char = s[right];
        count[char] = (count[char] || 0) + 1;

        maxCount = Math.max(maxCount, count[char]);

        while ((right - left + 1) - maxCount > k) {
            count[s[left]]--;
            left++;
        }

        maxLen = Math.max(maxLen, right - left + 1);
    }

    return maxLen;
};

console.log(characterReplacement("ABAB",2))
console.log(characterReplacement("AABABBA",1))

