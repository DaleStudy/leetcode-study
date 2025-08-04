/*
    - 각 비트 중 하나만 1일 때 1이 되므로 XOR연산 활용
    - 각 비트 둘 다 1일 때 올림수가 발생하므로 &연산 활용
    - a는 이제까지의 합 비트가 되고 
        b는 다음 자리에서 더해줘야 될 올림 비트가 됨.
        올림 비트 b가 0이 될 때까지 반복
	시간 복잡도는 O(1), 공간 복잡도는 O(1)
*/

class Solution {
	public:
		int getSum(int a, int b) {
	
			while (b != 0) {
				// 올림수 계산
				int carry = (a & b) << 1;
				// 올림 무시한 합 비트 계산
				a = a ^ b;
				// 다음 반복에 carry 더해주기
				b = carry;
			}
			return (a);
		}
	};
