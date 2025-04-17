class Solution {
    public boolean isAnagram(String s, String t) {        
	// 속도: 443ms

        // 길이가 같을 때 탐색 시작, 다르면 false
        if(s.length() == t.length()) {
            List<String> sList = new ArrayList<>(Arrays.asList(s.split("")));
            
            // t 각 문자에 대해 sList에서 제거 시도
            for (String ch : t.split("")) {
                // remove(ch)는 해당 ch가 있으면 제거하고 true를 반환, 없으면 false를 반환
                if (!sList.remove(ch)) {
                    return false;
                }
            }
            return true;
        }
        return false;
    }
}

