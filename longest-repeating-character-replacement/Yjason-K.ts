/**
 * sliding window
 * 문자열 k번 변경 가능한, 가장 긴 반복 문자열의 길이 구하기.
 * @param {string} s - 문자열
 * @param {number} k - 문자 변경 가능 횟수
 * @return {number} - 가장 긴 부분 문자열의 길이
 * 
 * 시간 복접도: O(n)
 *  - 문자길이 만큼의 1회 순회
 * 
 * 공간 복잡도: O(1)
 *  - 알파벳 26개의 제한된 Map 사용
 * 
 */
function characterReplacement(s: string, k: number): number {
    // 문자의 빈도를 저장할 Map
    const charFreq = new Map<string, number>();

    // window 왼쪽 포인터
    let left = 0;

    // 최대 길이, 최대 빈도 초기화
    let maxLength = 0;
    let maxFreq = 0;

    // 오른쪽 포인터를 0부터 이동하며 window 크기 조절
    for (let right = 0; right < s.length; right++) {
        const char = s[right];
        
        // 현재 문자의 빈도 증가
        charFreq.set(char, (charFreq.get(char) || 0) + 1);

        // 윈도우 내에서 가장 많이 등장한 문자의 빈도 갱신
        maxFreq = Math.max(maxFreq, charFreq.get(char)!);

        // 조건: (윈도우 크기 - maxFreq > k)일 때, 왼쪽 포인터 이동
        if (right - left + 1 - maxFreq > k) {
            const leftChar = s[left];
            charFreq.set(leftChar, charFreq.get(leftChar)! - 1); // 왼쪽 문자 제거
            left++; // 윈도우 축소
        }

        // 현재 윈도우 크기를 기준으로 최대 길이 갱신
        maxLength = Math.max(maxLength, right - left + 1);
    }

    return maxLength;

}

