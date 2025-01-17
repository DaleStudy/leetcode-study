/**
 * @description 문자열 배열을 하나의 문자열로 인코딩합니다.
 * @param {string[]} strs - 문자열 배열
 * @returns {string} 인코딩된 문자열
 *
 * 시간 복잡도: O(N)
 *  - N은 입력 배열의 모든 문자열 길이의 합
 * 공간 복잡도: O(1)
 *  - 추가 메모리 사용 없음
 */
function encode(strs: string[]): string {
    return strs.join(':');
  }
  
  /**
   * @description 인코딩된 문자열을 다시 문자열 배열로 디코딩합니다.
   * @param {string} s - 인코딩된 문자열
   * @returns {string[]} 디코딩된 문자열 배열
   *
   * 시간 복잡도: O(N)
   *  - N은 입력 문자열의 길이
   * 공간 복잡도: O(1)
   *  - 추가 메모리 사용 없음
   */
  function decode(s: string): string[] {
    return s.split(':');
  }

