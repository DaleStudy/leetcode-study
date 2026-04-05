class Solution {
  /**
   * @param {string[]} strs
   * @returns {string}
   */
  encode(strs) {
      return strs.map((str) => `${str.length}#${str}`).join('');
  }

  /**
   * @param {string} str
   * @returns {string[]}
   */
  decode(str) {
      const result: string[] = [];
      let i = 0;
      while(i < str.length) {
          const j = str.indexOf('#', i);
          const length = Number(str.slice(i, j));
          result.push(str.slice(j + 1, j + 1 + length));
          i = j + 1 + length;
      }
      return result;
  }
}
