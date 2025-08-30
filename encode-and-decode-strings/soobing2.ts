/**
 * 문제 유형
 * - String
 *
 * 문제 설명
 * - 문자열 인코딩과 디코딩
 *
 * 아이디어
 * 1) "길이 + # + 문자열" 형태로 인코딩
 *
 */
class Solution {
  /**
   * @param {string[]} strs
   * @returns {string}
   */
  encode(strs) {
    return strs.map((str) => `${str.length}#${str}`).join("");
  }

  /**
   * @param {string} str
   * @returns {string[]}
   */
  decode(str) {
    const result = [];
    let tempStr = str;
    while (tempStr.length) {
      let i = 0;

      while (tempStr[i] !== "#") {
        i++;
      }

      const length = Number(tempStr.slice(0, i));
      const currentStr = tempStr.slice(i + 1, i + 1 + length);
      result.push(currentStr);
      tempStr = tempStr.slice(length + i + 1);
    }
    return result;
  }
}
