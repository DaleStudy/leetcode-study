/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 * 
 */

var isAnagram = function (s, t) {
  // 두 문자열의 길이가 같지않다면 false
  if (s.length !== t.length) {
    return false;
  };

  // Map을 사용해서 데이터 최신화
  let count = new Map();

  // set으로 해당 문자를 key, 갯수를 value로 카운트
  for (let char of s) {
    count.set(char, (count.get(char) || 0) + 1)
  }

  for (let char of t) {
    // 새로운 문자가 map에 없거나, 이미 카운트가 0이라면 false
    if (!count.has(char) || count.get(char) === 0) {
      return false;
    }
    // 문자 카운트 -1
    count.set(char, (count.get(char) - 1))
  }

  return true;
}

/*
 * 문제: 두 문자열의 구성요소 비교
 * 
 * 생각: 각 문자열에 상대 문자열의 스펠링이 있는지 확인하고 splice로 제거
 * 결과: 타임리밋 
var isAnagram = function (s, t) {
  if (s.length !== t.length) {
    return false;
  };

  let sArr = [];
  let tArr = [];
  let finder = 0;

  for (let j = 0; j < s.length; j++) {
    sArr.push(s[j]);
    tArr.push(t[j]);
  }

  // 반복문을 돌며 s와 t를 비교
  for (let i = 0; i < s.length; i++) {
    //s[i]번 째가 t안에 있다면?
    if (tArr.indexOf(sArr[0]) !== -1) {
      // 찾은 인덱스를 저장해 줌 -> sArr 에서 splice먼저해버리면 배열이 달라져서 못찾음;;
      finder = tArr.indexOf(sArr[0]);
      //s[i]를 스플라이스로 빼고
      sArr.splice(0, 1);
      //t의 인덱스번호를 슬라이스로 뺌
      tArr.splice(finder, 1);
    }
    console.log(i);
    console.log(sArr);
    console.log(tArr);
  }

  // s와 t의 길이가 0이면 true 아니면 fales
  if (sArr.length === 0 && tArr.length === 0) {
    return true;
  }
  else return false

};

*/
