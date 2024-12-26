/*
runtime 12 ms, beats 4.87%
memory 60.49 MB, beats 5.89%

time complexity: O(n)
- nums 각각의 원소를 소인수분해 : O(10 * n) = O(n)
- ans[] 배열 계산 : O(n)

space complexity: O(n)
- 2차원 배열(n * 10) - powers : O(n)
- 1차원 배열들(n) - minuses, ans: O(n)

[풀이]
나눗셈이 금지되어 있기 때문에, 최대한 곱할 수 있는 만큼을 미리 곱해놓고, i번째 원소마다 부족한 부분만큼을 나중에 채워 넣어 곱해주는 방식으로 접근했습니다.
nums[i]의 절대값이 30 이하인 점에 착안해서, nums[i]는 많아야 10개의 base로 소인수 분해가 가능하다는 점을 떠올렸습니다. 따라서 각각의 base마다 (nums 전체에서 등장한 base의 지수의 총합) - (nums[i]의 base의 지수 중 가장 큰 값) 만큼의 지수로 미리 곱해주고, i에 대한 iteration에서 부족한 지수만큼을 보충해서 곱해주었습니다.
(풀이를 쓰다 보니, 실제 코드에서 이렇게 미리 곱해 놓은 수를 base라고 명명한 게 혼동될 수 있겠네요...^^;)

이 풀이에서 아쉬운 점이 여전히 있습니다. 시간 복잡도를 따지면 O(10*n) = O(n)이니 문제의 조건을 맞췄다고 할 수도 있겠지만, 상수가 좀 크다는 점이 마음에 걸리네요.
(for (int j = 0; j < 10 && abs > 1; j++) <--- 여기에서 abs == 1이 되면 for-loop를 빠져나가게 했지만, nums[i]가 모두 29로 차있는 edge case라면 10*n을 꽉 채우게 되니까요.)

이 풀이 말고도, nums[]를 2개로 나눈 블럭, 4개로 나눈 블럭, 8개로 나눈 블럭, ... 이런 식으로 사이즈 별로 블럭을 나눠두고, 각각의 블럭 내부의 곱을 미리 계산해두는 방식도 생각해보았습니다. 이러면 시간 복잡도와 공간 복잡도가 모두 O(nlogn)이 나올 것 같습니다. (사실 이 풀이를 가장 처음에 떠올렸습니다만, O(n)으로 줄이는 고민을 하다가 현재 제출한 풀이를 떠올리고서는 이 풀이는 구현을 안 했습니다. 시간이 되면 이렇게도 풀어보고, 좀 더 디벨롭을 해봐야겠네요.)
*/
class Solution {
    public int[] productExceptSelf(int[] nums) {
        int n = nums.length;

        int[] primes = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29};
        int[][] powers = new int[n][10];
        int[] sumPowers = new int[10];
        int[] maxPowers = new int[10];

        boolean[] minuses = new boolean[n];

        int base = 1;

        int[] ans = new int[n];

        for (int i = 0; i < n; i++) {
            if (nums[i] == 0) {
                int x = 1;
                for (int j = 0; j < n; j++) {
                    if (j == i) {
                        continue;
                    }
                    ans[j] = 0;
                    x *= nums[j];
                }
                ans[i] = x;

                return ans;
            }

            int abs;
            if (nums[i] > 0) {
                abs = nums[i];
            } else {
                abs = -nums[i];
                base = -base;
                minuses[i] = true;
            }

            for (int j = 0; j < 10 && abs > 1; j++) {
                int curPower = 0;
                while (abs % primes[j] == 0) {
                    powers[i][j]++;
                    sumPowers[j]++;
                    curPower++;
                    abs /= primes[j];
                }
                if (curPower > maxPowers[j]) {
                    maxPowers[j] = curPower;
                }
            }
        }

        for (int i = 0; i < 10; i++) {
            for (int j = 0; j < sumPowers[i] - maxPowers[i]; j++) {
                base *= primes[i];
            }
        }

        for (int i = 0; i < n; i++) {
            ans[i] = base;
            for (int j = 0; j < 10; j++) {
                for (int k = 0; k < maxPowers[j] - powers[i][j]; k++) {
                    ans[i] *= primes[j];
                }
            }
            if (minuses[i]) {
                ans[i] = -ans[i];
            }
        }


        return ans;
    }
}
