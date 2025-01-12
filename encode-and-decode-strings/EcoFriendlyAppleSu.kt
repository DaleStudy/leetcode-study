package leetcode_study

/*
* 문자열 인코딩 디코딩 문제
* 시간 복잡도: O(n)
* 공간 복잡도: O(n)
* */
fun encoding(strs: List<String>): String {
    var result = ""
    if (strs.isEmpty()) return result
    for (index in 0 until strs.size - 1) {
        if (strs[index] == ":") {
            result += strs[index] + "::;"
        } else {
            result += strs[index] + ":;"
        }
    }
    result += strs[strs.size - 1]
    return result
}

fun decoding(str: String): List<String>{
    val splitedStrList = str.split(":;")
    val result = mutableListOf<String>()
    for (splitStr in splitedStrList){
        if (splitStr == "::") {
            result.add(":")
        } else {
            result.add(splitStr)
        }
    }
    return result
}
