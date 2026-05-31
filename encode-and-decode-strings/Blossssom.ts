class Solution {
  private baseStr = "#";
  /*
   * @param strs: a list of strings
   * @return: encodes a list of strings to a single string.
   */
  public encode(strs: string[]): string {
    let encodedStr = "";
    for (const str of strs) {
      encodedStr += `${str.length}${this.baseStr}${str}`;
    }
    return encodedStr;
  }

  /*
   * @param str: A string
   * @return: decodes a single string to a list of strings
   */
  public decode(str: string): string[] {
    const spliter = [];
    let idx = 0;
    while (idx < str.length) {
      let findBase = idx;
      // length가 10 이상일 경우를 위해 순회하며 파싱
      while (str[findBase] !== this.baseStr) {
        findBase++;
      }

      const contentLength = parseInt(str.substring(idx, findBase));
      const content = str.substring(findBase + 1, findBase + contentLength + 1);
      spliter.push(content);
      idx = findBase + contentLength + 1;
    }
    return spliter;
  }
}

const input = ["lint", "code", "love", "you"];

const solutionInstance = new Solution();

const encoded = solutionInstance.encode(input);
const decoded = solutionInstance.decode(encoded);

console.log(encoded, decoded);


