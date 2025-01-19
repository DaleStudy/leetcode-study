/*
 * 시간복잡도 : O(n)
 * - 배열 1회 순회하면서 문자열 합치기
 *
 * 공간복잡도 : O(1)
 */
function encode(strs: string[]): string {
  let result = strs[0];

  for (let i = 1; i < strs.length; i++) {
    result += "#" + strs[i];
  }
  return result;
}
/*
 * 시간복잡도 : O(n)
 * - 문자 순회하면서 # 기준으로 나눔
 *
 * 공간복잡도 : O(n)
 * - 문자열 길이만큼 생성해서 리턴
 */
function decode(encoded: string): string[] {
  return encoded.split("#");
}

// 스택 활용하는 방법
/*
 * 시간복잡도 : O(n)
 *
 * 공간복잡도 : O(1)
 */

// ["Hello","World"] => 5#Hello5#World
function encode(strs: string[]): string {
  let result = "";
  for (const str of strs) {
    result += `${str.length}#${str}`;
  }
  return result;
}

/*
 * 접근 방법 :
 * - 배열 길이를 포함해서 encode한 뒤 decode할 때 길이 활용헤서 stack에 담는 방식
 *
 * 시간복잡도 : O(n)
 * - 인코딩된 문자열 1회 순회
 *
 * 공간복잡도 : O(n)
 * - n은 result 길이
 */

// 5#Hello5#World => ["Hello","World"]
function decode(encoded: string): string[] {
  const result: string[] = [];
  let index = 0;
  while (index < encoded.length) {
    const separatorIndex = encoded.indexOf("#", index);
    const length = parseInt(encoded.slice(index, separatorIndex), 10);
    index = separatorIndex + 1;
    const str = encoded.slice(index, index + length);
    result.push(str);
    index += length;
  }

  return result;
}
