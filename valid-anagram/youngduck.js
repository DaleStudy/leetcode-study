/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isAnagram = function (s, t) {
    const mapS = new Map();
    const mapT = new Map();
  
    [...s].map((item) => {
      if (mapS.has(item)) {
        const itemCount = mapS.get(item);
        mapS.set(item, itemCount + 1);
      } else {
        mapS.set(item, 1);
      }
    });
  
    [...t].map((item) => {
      if (mapT.has(item)) {
        const itemCount = mapT.get(item);
        mapT.set(item, itemCount + 1);
      } else {
        mapT.set(item, 1);
      }
    });
  
    // NOTE -  t가 s의 anagram이라는 뜻을 갯수가 같지않아도 된다고 이해했으나 anagram정의는 s구성원을 모자람,남김없이 t를만들 수 있는 상태
    if (mapS.size !== mapT.size) {
      return false;
    }
  
    for (const [key, value] of mapS) {
      if (mapT.get(key) !== value) {
        return false;
      }
    }
  
    return true;
  };

  // 시간복잡도: O(n)
  // - 문자열 s와 t를 각각 한 번씩 순회: O(n) + O(n) = O(2n) = O(n)
  // - Map 비교를 위한 순회: O(k), 여기서 k는 고유 문자 개수
  // - 따라서 전체 시간복잡도는 O(n)
  // 공간복잡도: O(1)
  // - 두 개의 Map 객체 생성: mapS와 mapT
  // - 각 Map은 최대 k개의 고유 문자를 저장 (k는 고유 문자 개수)
  // - 소문자 영문자만 사용하므로 k ≤ 26 (a-z)
  // - 따라서 전체 공간복잡도는 O(1) (상수 시간)

  // follow up: 유니코드 테스트 케이스. 큰 의미는 없음
  console.log(isAnagram("😀😀", "😀😀😀"));
  // false
  console.log(isAnagram("한글글", "글한글"));
  // true
  console.log(isAnagram("café", "éfac"));
  // true
  console.log(isAnagram("Hello世界", "世界Hello"));
  // true
  console.log(isAnagram("안녕 하세요", "하세요 안녕"));
  // true
  console.log(isAnagram("Café", "éfac"));
  // false
  console.log(isAnagram("Café", "Éfac"));
  // false