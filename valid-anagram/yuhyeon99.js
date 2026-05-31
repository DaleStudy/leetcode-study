/**
 * 2 개의 문자열 s와 t가 주어진다. 만약 t가 s의 anagram일 경우 true를 반환하고 그렇지 않은 경우 false를 반환하는 함수
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isAnagram = function(s, t) {
  var sMap = new Map();
  var tMap = new Map();

  for(let e of [...s]) {
      if(sMap.has(e)) {
          sMap.set(e, sMap.get(e) + 1);
      } else {
          sMap.set(e, 1);
      }
  }

  for(let e of [...t]) {
      if(tMap.has(e)) {
          tMap.set(e, tMap.get(e) + 1);
      } else {
          tMap.set(e, 1);
      }
  }

  if(sMap.size > tMap.size) {
      for(let s of sMap) {
          if(tMap.get(s[0]) && tMap.get(s[0]) === s[1]) continue;
          return false;
      }
  } else {
      for(let t of tMap) { 
          if(sMap.get(t[0]) && sMap.get(t[0]) === t[1]) continue;
          return false;
      }
  }

  return true;
};
