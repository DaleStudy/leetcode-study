/*
    풀이 :
        특정 칸에 오는 방법은 왼쪽에서 오거나 위에서 오거나 둘 중 하나이므로 두 곳의 unique path 개수를 더하면 구할 수 있다
        한 row 만들고 두번쨰 줄부터 그 이전 값(위에서 오는 개수)과 그 전 index의 값(왼쪽에서 오는 개수)를 더하면서 반복한다
        최종적으로 row의 가장 오른쪽 값 return

    row크기 = M, col 크기 = N

    TC : O(M * N)
        모든 칸에 대해 순회

    SC : O(N)
        한 row만큼 메모리 할당
*/

#include <vector>
using namespace std;

class Solution {
public:
    int uniquePaths(int m, int n) {
        vector<int> row(n, 1);

        for (int i = 1; i < m; i++) {
            for (int j = 1; j < n; j++) {
                row[j] = row[j] + row[j - 1];
            }
        }
        return row[n - 1];
    }
};
