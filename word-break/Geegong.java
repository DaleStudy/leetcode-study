import java.util.Arrays;
import java.util.HashSet;
import java.util.List;

public class Geegong {

    /**
     * string segmentation 을 이용해서 풀어햐한다.
     * dp를 이용해 segmentation 이 된 지점을 true 로 저장하면서 s 이 length 인덱스의 값이 true 로 되어있는지 체크
     * Time complexity : O (N^3) 🥲
     * -> 이중 루프 (N^2) * contains(substring) (N)
     *
     * Space complexity : O(N)
     * @param s
     * @param wordDict
     * @return
     */
    public boolean wordBreak(String s, List<String> wordDict) {
        HashSet<String> distinctWords = new HashSet<>(wordDict);

        // 1 = true, 0 = false
        int[] dp = new int[s.length() + 1];
        Arrays.fill(dp, 0);
        dp[0] = 1;

        for (int rightIndex = 1; rightIndex <= s.length() ; rightIndex++) {
            for (int leftIndex = 0; leftIndex < rightIndex; leftIndex++) {
                if (dp[leftIndex] == 1 && distinctWords.contains(s.substring(leftIndex, rightIndex))) {
                    dp[rightIndex] = 1;
                }
            }
        }

        return dp[s.length()] == 1;
    }

}

