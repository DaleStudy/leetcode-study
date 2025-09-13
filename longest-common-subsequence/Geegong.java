import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;
import java.util.List;

public class Geegong {

    /**
     * LIS, LCS 와 연관지어서 풀이
     * 1. 먼저 text1을 훑어보는데 text1에 중복되는 알파벳이 있을 수 있기에 각 캐릭터별로 인덱스들을 저장 (각 원소가 arrayList가 있는 배열)
     * 2. text2 를 훑으면서 매칭되는 캐릭터들에 대해서만 1에서 저장된 인덱스들을 한 배열안에 나열
     * -> 이떄 나열해서 넣을때마다 역순으로 집어넣는게 중요! (왜냐면 이 나열된 인덱스들을 가지고 LIS를 구할거라서)
     * 3. 나열된 인덱스들의 값들을 가지고 LIS 를 구한다, 즉 이 LIS의 길이가 LCS 의 길이가 된다..!! (와우 신기)
     * 그러나 leet code 에 돌렸을 때 runtime 이 영 좋지는 않음
     *
     * time complexity : O(M + N logN) => text2에 대해서 문자마다 바이너리서치가 수행됨
     * space complexity : O(M+N)
     * @param text1
     * @param text2
     * @return
     */
    public int longestCommonSubsequence(String text1, String text2) {
        char[] chText1 = text1.toCharArray();
        char[] chText2 = text2.toCharArray();

        // text1만 각 원소 별로 char가 가지는 index를 array 로 갖는 배열을 생성
        List<Integer>[] positionIndices = new List[26];
        for (int index = 0; index<chText1.length; index++) {
            if (positionIndices[chText1[index] - 'a'] == null) {
                positionIndices[chText1[index] - 'a'] = new ArrayList();
                positionIndices[chText1[index] - 'a'].add(index);
            } else {
                positionIndices[chText1[index] - 'a'].add(index);
            }
        }


        // 여기서부터 LIS 를 구할것임
        List<Integer> indices = new ArrayList<>();
        for (int index=0; index<chText2.length; index++) {

            char find = chText2[index];
            if (positionIndices[find-'a'] != null && positionIndices[find-'a'].size() > 0) {
                // 역순 (LIS 를 구하기 위해서 일부러 뒤집어 높음, 즉 각 char 별 LIS 를 구할것이기 때문에..)
                // positionIndices 에서 구했던 값들을 그대로 addAll 한다면 오름차순이 되기때문에 정확한 LIS 를 구할 수 없다

                indices.addAll(positionIndices[find-'a'].stream().sorted(Comparator.reverseOrder()).toList());
            }
        }

        // find LIS
        return findLIS(indices).size();
    }

    public List<Integer> findLIS(List<Integer> source) {
        if (source.size() == 0) {
            return source;
        }

        List<Integer> LISResult = new ArrayList<>();
        for (int index=0; index<source.size(); index++) {
            int target = source.get(index);
            int insertionPosition = Collections.binarySearch(LISResult, target);
            //Returns:
            //the index of the search key, if it is contained in the list;
            // otherwise, (-(insertion point) - 1). The insertion point is defined as the point at which the key would be inserted into the list:
            if (insertionPosition < 0) {
                insertionPosition = -insertionPosition - 1;
            }

            if (LISResult.size() == insertionPosition) {
                LISResult.add(target);
            } else {
                LISResult.set(insertionPosition, target);
            }
        }

        return LISResult;
    }

}

