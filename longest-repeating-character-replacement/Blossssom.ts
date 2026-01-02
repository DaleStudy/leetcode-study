/**
 * @param s - 대문자 알파벳 문자열
 * @param k - 문자열을 바꿀 수 있는 횟수
 * @returns - 동일 문자를 포함한 가장 긴 문자열의 길이
 */
function characterReplacement(s: string, k: number): number {
  const countMap = new Map<string, number>();

  let left = 0;
  let maxRepeatCount = 0;
  let maxLength = 0;

  for (let right = 0; right < s.length; right++) {
    const char = s[right];

    // 문자 카운트 누적
    countMap.set(char, (countMap.get(char) || 0) + 1);

    maxRepeatCount = Math.max(maxRepeatCount, countMap.get(char)!);

    // (현재 윈도우 길이 - 최대 빈도수) 가 k 보다 크면 윈도우 축소 => left 증가
    while (right - left + 1 - maxRepeatCount > k) {
      const leftChar = s[left];
      countMap.set(leftChar, countMap.get(leftChar)! - 1);
      left++;
    }

    // 유효한 윈도우 중 최대 길이
    maxLength = Math.max(maxLength, right - left + 1);
  }

  return maxLength;
}

const s = "ABAB";
const k = 2;
characterReplacement(s, k);


