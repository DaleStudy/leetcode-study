class Solution {
  /**
   * 시간 복잡도: strs의 길이만큼 순회하므로, O(n)
   * 공간 복잡도: 결괏값 제외 추가 변수 사용 없으므로 O(1)
   */
  /**
   * @param {string[]} strs
   * @returns {string}
   */
  encode(strs) {
      return strs.reduce((acc, cur) => acc+ `${cur.length}` + '!' + cur, '');
  }

  /**
   * 시간 복잡도: str의 길이만큼 순회하므로 str의 길이가 m이면, O(m)
   * 공간 복잡도: 결괏값 제외 상수 크기 변수만 사용하므로, O(1)
   */
  /**
   * @param {string} str
   * @returns {string[]}
   */
  decode(str) {
      const res = [];
      let i = 0;
      while (i < str.length) {
          let j = i;
          while (str[j] !== '!') {
              j++;
          }
          const len = Number(str.slice(i, j));
          const s = str.slice(j + 1, j + 1 + len);
          res.push(s);
          i = j + 1 + len;
      }
      return res;
  }
}
