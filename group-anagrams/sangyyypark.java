/**
 1. 문제이해
 anagrams는 단어가 있을때 단어에 포함된 알파벳 빈도수가 모두 동일한것을 의미합니다.
 group anagrams는 list에 단어목록이 있을때 anagrams이 되는 단어들을 배열로 그룹핑한 리스트 입니다.

 2. naive algorithm도출

 O(N^2) 방법
 2.1.단어 하나를 선택하고, 해당 단어의 빈도수를 저장하는 Map을 생성합니다.
 2.2해당 단어를 제외하고 나머지 단어들을 탐색하면서 동일한 빈도수를 가진 단어들을 새로운 list에 저장합니다.

 개선포인트
 각 단어를 알파벳 오름차순으로 정렬

 */
class sangyyypark {
    public List<List<String>> groupAnagrams(String[] strs) {
        Map<String,List<String>> map = new HashMap<>();
        for(String str : strs) {
            String key = sortedString(str);
            List<String> group = map.get(key);
            if(group != null) {
                group.add(str);
            }
            else {
                List<String> newGroup = new ArrayList<>();
                newGroup.add(str);
                map.put(key, newGroup);
            }
        }

        return new ArrayList<>(map.values());
    }

    public String sortedString(String str) {
        char [] charArr = str.toCharArray();
        Arrays.sort(charArr);
        return new String(charArr);
    }
}

