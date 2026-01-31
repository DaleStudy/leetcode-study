func getSum(a int, b int) int {
    for b != 0 {
        sumWithoutCarry := a ^ b
        carry := (a & b) << 1

        a = sumWithoutCarry
        b = carry
    }
    return a
}


