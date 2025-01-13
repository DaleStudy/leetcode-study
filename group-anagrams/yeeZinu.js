/**
 * @param {string[]} strs
 * @return {string[][]}
 */
var groupAnagrams = function (strs) {
  // 정답 객체
  let ans = {};

  for (let s of strs) {
      // strs 배열에서 받아온 s를 하나씩 쪼개서 정렬, 다시 하나로 뭉침
      let key = s.split('').sort().join('');

      // 만약 정답 객체에 현재 단어가 없다?
      if (!ans[key]) {
          // 해당 값을 빈 배열로 초기화
          ans[key] = [];
      }
      // 해당 값 배열에 초기 단어 추가.
      ans[key].push(s);
  }
  // 객체에 값을 추가한 것이기 때문에 Object.value()를 사용해서 열거 가능한 배열로 리턴
  return Object.values(ans);
};
