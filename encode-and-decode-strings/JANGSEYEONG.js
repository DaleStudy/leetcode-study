/**
 * 시간 복잡도: O(n) - n은 모든 문자열의 총 길이. 각 문자를 한 번씩만 처리함
 * 공간 복잡도: O(n) - 인코딩/디코딩 결과를 저장하는 데 원본 데이터 크기만큼 공간 필요
 */
var encode = function (strs) {
  let text = "";
  for (let str of strs) {
    // 각 문자열 앞에 길이와 구분자(:)를 붙여서 저장
    // 예: ["abc", "de"] -> "3:abc2:de"
    text += `${str.length}:${str}`;
  }
  return text;
};

var decode = function (s) {
  const result = [];
  let start = 0;

  while (start < s.length) {
    // 가장 첫번째에 등장하는 콜론 위치를 찾아 길이 정보 추출
    const mid = s.indexOf(":", start);
    const length = parseInt(s.substring(start, mid));

    // 길이 정보를 이용해 원래 문자열 추출하여 결과 배열에 추가
    result.push(s.substring(mid + 1, mid + 1 + length));

    // 다음 문자열의 시작 위치로 이동
    start = mid + 1 + length;
  }

  return result;
};
