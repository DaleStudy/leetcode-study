class Solution {
  /**
   * 문자열 배열을 하나의 문자열로 인코딩합니다.
   * @param strs - 문자열 배열
   * @returns 인코딩된 하나의 문자열
   */
  encode(strs: string[]): string {
    return strs.map((str) => str.length + "#" + str).join("");
  }

  /**
   * 인코딩된 문자열을 원래 문자열 배열로 디코딩합니다.
   * @param str - 인코딩된 문자열
   * @returns 디코딩된 문자열 배열
   */
  decode(str: string): string[] {
    const result: string[] = [];

    let i = 0;
    while (i < str.length) {
      let j = i;
      while (str[j] !== "#") {
        j++;
      }

      const length = parseInt(str.slice(i, j));
      const word = str.slice(j + 1, j + 1 + length);
      result.push(word);
      i = j + 1 + length;
    }

    return result;
  }
}
