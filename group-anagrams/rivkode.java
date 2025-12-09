/*
1. 문제 이해
strs로 들어오는 인풋들에 대해 동일한 문자를 사용해서 대체할 수 있는지 체크
대체할 수 있으면 하나의 그룹으로 묶어서 List 생성
생성한 그룹들을 모아서 다시 하나의 2차원 리스트로 반환

2. 알고리즘
2중 for loop인데 조건을 보니까
탐색을 10^4 * 100 이면 10^6 이므로 1,000,000 이니까
해볼만 한 것 같다.

3. 구현
각 글자들을 정렬해서 기존과 같은 인덱스를 가지는 hashmap 생성

글자가 같은지 비교
같은 글자의 인덱스를 체크해서 기존 리스트에서 해당 글자를 넣음
없으면 본인만 넣음

반환

아니다 ..
답지 참고하니 HashMap을 사용하고 있네
Map에서 key 로 sorted 된 단어를 넣고 value 로 일치하는 단어 리스트를 넣는다.

이렇게 되면 한번만 for loop 를 도는것이므로 리스트에서 제거하거나 하는 일이 없어도 된다.
그리고 구현도 깔끔하게 그리고 이해하기 쉽게 구현된다.

4. 예외
없을 경우 본인 넣기
글자는 소문자만 존재

*/

import java.util.*;

class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        Map<String, List<String>> anagrams = new HashMap<>();

        for (int i=0; i<strs.length; i++) {
            String w = strs[i];

            char[] arr = w.toCharArray();
            Arrays.sort(arr);
            String sorted = new String(arr);
            
            if (!anagrams.containsKey(sorted)) {
                anagrams.put(sorted, new LinkedList<>());
            }
            List<String> list = anagrams.get(sorted);
            list.add(w);
        }

        return new ArrayList<>(anagrams.values());

        // List<String> originLst = new ArrayList<>();
        // Map<Integer, String> hash = new HashMap<>();
        // List<List<String>> answer = new ArrayList<>();

        // for (int i=0; i<strs.length; i++) {
        //     String s = strs[i];
        //     originLst.add(s);
        //     char[] cArr = s.toCharArray();
        //     Arrays.sort(cArr);
        //     String orS = new String(cArr);
        //     hash.put(i, orS);
        // }

        // for (int i=0; i<orderLst.size(); i++) {
        //     List<String> tmp = new ArrayList<>();
        //     String s = orderLst.get(i);
        //     // 정답에 넣기
        //     tmp.add(originLst.get(i));
        //     for (int j=i; j<orderLst.size(); j++) {
        //         String compare = orderLst.get(j);
        //         if (s.equals(compare)) {
                    
        //             // 정답에 넣기
        //             tmp.add(originLst.get(j));
        //         }
        //     }
        //     answer.add(tmp);
        // }
        
        // return answer;
    }
}
