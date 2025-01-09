package leetcode_study

/*
* 주어진 32 bits unsigned integer를 뒤집는 문제
* Bit 연산에 대한 개념이 전무해 String으로 치환 후 문제 해결
* 작은 수는 표현할 수 있었지만 아래와 같이 문제를 해결할 경우 큰 수가 입력되었을 경우 부호 비트를 인식하여 음수로 표기합니다.
* 또한 32 bit를 구성하기 위해 부족한 문자열을(자릿수) 추가하기 때문에 연산이 더해집니다.
* */
fun reverseBits1(n:Int):Int {
    val nStr = n.toString(2)
    val totalLength = nStr.length
    var temp = ""
    if (totalLength != 32) {
        for (i in 0 until 32 - totalLength) {
            temp += "0"
        }
    }
    val fullBitString = temp + nStr
    var result = 0

    for (i in (fullBitString.length - 1) downTo 0) {
        val eachBitValue = 2.0.pow(i).toInt()
        if (fullBitString[i] == '0') {
            continue
        } else {
            result += eachBitValue
        }
    }
    println(result.toString(2))
    return result
}

/*
* Bit 연산을 통한 Reverse Bit 구성
* 시간 복잡도: O(32) (32비트의 숫자에 대해 반복)
* 공간 복잡도: O(1) (상수 공간 사용)
* */
fun reverseBits(n: Int): Int {
    var input = n
    var result = 0

    for (i in 0 until 32) {
        // 결과에 현재 비트 추가
        result = (result shl 1) or (input and 1)
        // 입력 비트를 오른쪽으로 이동
        input = input shr 1
    }

    return result
}
