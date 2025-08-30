// 네트워크 전송을 위해서 문자열 리스트를 하나의 문자열로 안전하게 합치고
// 다시 분리하는 함수를 작성하세요.

/**
 풀이 과정:
 구분자를 "a,b,c"와 같이 ,로 join하면, 원래 문자열에 ,가 포함될 때 깨진다.
 따라서 길이 정보를 함께 저장하거나 특수 escape 문자를 써야한다. 


 */
/**
 * Encodes a list of strings to a single string.
 * @param {string[]} strs
 * @return {string}
 */
function encode(strs) {
  // 각 문자열 앞에 "길이#"를 붙임
  // 예: ["abc", "de"] -> "3#abc2#de"
  return strs.map((s) => `${s.length}#${s}`).join("");
}

/**
 * Decodes a single string to a list of strings.
 * @param {string} s
 * @return {string[]}
 */
function decode(s) {
  let res = [];
  let i = 0;

  while (i < s.length) {
    // 1. 길이 읽기
    let j = i;
    while (s[j] !== "#") j++;
    let length = parseInt(s.slice(i, j), 10);

    // 2. 길이에 맞춰 문자열 추출
    let str = s.slice(j + 1, j + 1 + length);
    res.push(str);

    // 3. 인덱스 이동
    i = j + 1 + length;
  }

  return res;
}
