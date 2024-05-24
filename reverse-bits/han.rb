# @param {Integer} n, a positive integer
# @return {Integer}
def reverse_bits(n)
    # 이유는 모르겠으나 문제 설명과는 달리 leetcode 루비 테스트코드에선 n이 10진수 Integer로 들어오네요.
    n.to_s(2).rjust(32,'0').reverse.to_i(2)
end
