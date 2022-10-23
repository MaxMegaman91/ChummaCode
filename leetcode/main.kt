fun main(): {
    fun countSubarrays(nums: IntArray, minK: Int, maxK: Int): Long {
        var lower = -1
        var upperMin = -1
        var upperMax = -1
        var answer = 0L
        for ((j, x) in nums.withIndex()) {
            if (x < minK || x > maxK) {
                lower = j
            }
            if (x == minK) {
                upperMin = j
            }
            if (x == maxK) {
                upperMax = j
            }
            val pos = max(0, min(upperMin, upperMax) - lower)
            answer += pos.toLong()
        }
        return answer
    }

    countSubarrays()
}
