class Solution {
    fun solution(new_id: String) = new_id.toLowerCase()
        .filter { it.isLowerCase() || it.isDigit() || it == '-' || it == '_' || it == '.'  }
        .replace("[.]*[.]".toRegex(), ".")
        .removePrefix(".").removeSuffix(".")
        .let{ if (it.isEmpty()) "a" else it}
        .let{ if (it.length > 15) it.substring(0 until 15) else it }.removeSuffix(".")
        .let{
            if (it.length <= 2)
                StringBuilder(it).run{
                    while (length < 3) append(it.last())
                    toString()
                }
            else it}
}
