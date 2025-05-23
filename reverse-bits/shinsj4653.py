"""
[문제풀이]
# Inputs

# Outputs

# Constraints

# Ideas

[회고]

"""


class Solution:
    def reverseBits(self, n: int) -> int:
        st = []

        # while n > 0:
        #    st.append(n % 2)
        #    n //= 2  => 32 bit 길이 맞춰야함!

        while len(st) < 32:
            print('st.append: ', n % 2)
            st.append(n % 2)
            n //= 2

        ret, num = 0, 0
        print("st: ", st)

        # 6 : 110
        # [0 1 1]

        while st:
            print('st.pop(): ', st[-1])
            ret += st.pop() * (2 ** num)
            num += 1

        return ret


