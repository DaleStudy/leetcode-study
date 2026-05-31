/*
투 포인터 start와 end 생성, end를 1씩 증가하며 s를 탐색한다
각 문자열의 마지막 위치를 기록하는 locate Map을 생성한다
end값이 locate에 이미 존재하는데 start가 해당값+1보다 작을 경우, start를 해당값+1로 변경하고 locate를 업데이트, 이어서 탐색한다
매번 탐색마다 최대 길이 result를 갱신한다

시간복잡도 : O(N) - 단일 순회
공간복잡도 : O(N) (locate Map)


*/

function lengthOfLongestSubstring(s: string): number {
  let start = 0
  let end = 0
  const locate = new Map()
  let result = 0

  while (end < s.length) {
    let char = s[end]
    if (locate.has(char)) {
      start = Math.max(start, locate.get(char) + 1)
    }
    locate.set(char, end)
    result = Math.max(result, end - start + 1)
    end += 1
  }

  return result
}
