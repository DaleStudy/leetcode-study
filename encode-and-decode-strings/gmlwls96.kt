class Solution {

    fun encode(strs: List<String>): String {
        return strs.joinToString(separator = ":;") {
            if (it == ":") {
                "::"
            } else {
                it
            }
        }
    }

    fun decode(str: String): List<String> {
        return str
            .replace("::", ":")
            .split(":;")
    }
}