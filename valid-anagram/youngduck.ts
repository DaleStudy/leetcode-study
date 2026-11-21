// 시간복잡도 : O(n) - 문자열을 배열로 변환하고 각 문자의 빈도수를 한번씩 확인, n은 두 문자열 중 긴 길이
// 공간복잡도 : O(n) - 문자열을 복사한 배열 사용, 알파벳 빈도 배열은 길이가 26으로 고정

function isAnagram(s: string, t: string): boolean {
  // 문자열 배열로변환
  const sArray=[...s];
  const tArray=[...t];
  // 알파벳 인덱스를 배열로 할당해놓아서 빈도수만 올리게 처리 이중반복문을 없애기위해
  const sAlphabetIndex=[...new Array(26)].map((item,idx)=>0);
  const tAlphabetIndex=[...new Array(26)].map((item,idx)=>0);
  // 길이가다르면 반복문 돌기도전에 false 반환
  if(s.length!==t.length){
      return false;
  }
  // a~z의 charCodeAt값을 0~25에 맞추기위해 -97 처리하여 빈도수 추가
  for(let i = 0; i<s.length; i++){
      tAlphabetIndex[tArray[i].charCodeAt(0)-97]+=1;
      sAlphabetIndex[sArray[i].charCodeAt(0)-97]+=1;
  }

  // JavaScript의 경우 배열의 동등비교는 참조를 비교하므로 문자열로 변환해서 각 알파벳의 빈도수가 같은지 확인
  return JSON.stringify(tAlphabetIndex)===JSON.stringify(sAlphabetIndex);
};
