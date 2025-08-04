/**
 * 문자열 리스트를 하나의 문자열로 인코딩하고, 다시 디코딩 하기
 *
 * 접근 방법:
 * 길이 기반 인코딩 => 각 문자열마다 "길이#문자열" 형식으로 인코딩
 * "#"을 기준으로 문자열을 나누고, 길이를 이용해 원래 문자열을 복원하여 디코딩
 */

/**
 * @param {string[]} strs - 인코딩할 문자열 리스트
 * @return {string} - 인코딩된 문자열
 */
var encode = function (strs) {
  if (!strs || strs.length === 0) return '';
  return strs.map((str) => str.length + '#' + str).join('');
};

/**
 * @param {string} s - 디코딩할 인코딩된 문자열
 * @return {string[]} - 원래의 문자열 리스트
 */
var decode = function (s) {
  if (!s || s.length === 0) return [];

  const result = [];
  let i = 0;

  while (i < s.length) {
    const delimiterIndex = s.indexOf('#', i); // '#'의 위치 찾기
    const length = parseInt(s.slice(i, delimiterIndex)); // 길이 추출

    const start = delimiterIndex + 1; // 문자열 시작 위치
    result.push(s.slice(start, start + length)); // 알아낸 길이만큼 문자열 추출 후 결과에 추가
    i = start + length; // 다음 문자열 시작 위치로 포인터 이동
  }

  return result;
};
