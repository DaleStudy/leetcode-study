/**
 * 
 * @problem
 * 문자열 배열을 단일 문자열로 인코딩하고, 
 * 다시 원래의 문자열 배열로 디코딩하는 기능을 만들어야 합니다.
 * 
 * @example
 * const encoded = encode(["hello", "world"]);
 * console.log(encoded); // "5?hello5?world"
 * const decoded = decode(encoded);
 * console.log(decoded); // ["hello", "world"]
 * 
 * @description
 * - 시간 복잡도:
 *   ㄴ encode: O(n) (n은 문자열 배열의 총 길이)
 *   ㄴ decode: O(n) (n은 인코딩된 문자열의 길이)
 * - 공간 복잡도:
 *   ㄴ encode: O(1) (추가 메모리 사용 없음)
 *   ㄴ decode: O(1) (결과 배열을 제외한 추가 메모리 사용 없음)
 */

/**
 * @param {string[]} strs - 인코딩할 문자열 배열
 * @returns {string} - 인코딩된 문자열
 */
const encode = (strs) => {
  let encoded = '';
  for (const str of strs) {
    // 문자열을 "길이?문자열" 형식으로 추가
    encoded += `${str.length}?${str}`;
  }
  return encoded;
};

/**
 * @param {string} s - 인코딩된 문자열
 * @returns {string[]} - 디코딩된 문자열 배열
 */
const decode = (s) => {
  const result = [];
  let i = 0;

  while (i < s.length) {
    // 현재 위치에서 숫자(길이)를 읽음
    let length = 0;
    while (s[i] !== '?') {
      length = length * 10 + (s[i].charCodeAt(0) - '0'.charCodeAt(0)); // 숫자 계산
      i++;
    }

    // '?' 이후의 문자열을 추출
    i++; // '?'를 건너뜀
    const str = s.substring(i, i + length);
    result.push(str);

    // 다음 문자열로 이동
    i += length;
  }

  return result;
};

const encoded = encode(["hello", "world"]);
console.log(encoded); // "5?hello5?world"

const decoded = decode(encoded);
console.log(decoded); // ["hello", "world"]
