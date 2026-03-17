function isAnagram(s: string, t: string): boolean {
  if(s.length !== t.length) return false;
  
  const sMap = new Map<string, number>();
  const tMap = new Map<string, number>();

  for(const s_char of s) {
      sMap.set(s_char, (sMap.get(s_char) ?? 0) + 1);
  }

  for(const t_char of t) {
      tMap.set(t_char, (tMap.get(t_char) ?? 0) + 1);
  }

  if(sMap.size !== tMap.size) return false;
  for(const [sKey, sValue] of sMap) {
      if(sValue !== tMap.get(sKey)) return false;
  }
  return true
};
