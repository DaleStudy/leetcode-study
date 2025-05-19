// idea: 배열에 담긴 모든 애들을 다 sorting하면서 sorting된 결과를 key로 바인딩하고 Record<string, string[]> 에 맞게 매핑하여 values들만 리턴하면 될것 같음
function groupAnagrams(strs: string[]): string[][] {
  const map = new Map<string, string[]>();

  for (let i = 0; i < strs.length; i++) {
    const key = strs[i].split("").sort().join("");
    const group = map.get(key);
    if (group) {
      group.push(strs[i]);
    } else {
      map.set(key, [strs[i]]);
    }
  }
  return [...map.values()];
}
