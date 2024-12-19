import java.util.HashSet;

public class Solution {
	public int longestConsecutive(int[] nums) {
		HashSet<Integer> set = new HashSet<>();
		for (int num : nums) {
			set.add(num);
		}

		int maxStreak = 0;

		for (int num : nums) {
			// 내가 시작 값이라면
			if (!set.contains(num - 1)) {
				int currentNum = num;
				int currentStreak = 1;

				// 나로부터 연결되는 값을 찾는다.
				while (set.contains(currentNum + 1)) {
					currentNum++;
					currentStreak++;
				}

				maxStreak = Math.max(maxStreak, currentStreak);
			}
		}

		return maxStreak;
	}
}




