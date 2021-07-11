export function lengthOfLongestSubstring(s: string): number {
    let letterToPosition = {}
    let counter = 0
    let maxCounter = 0

    for (let i = 0; i < s.length; i++) {
        const letter = s[i]

        if (Number.isInteger(letterToPosition[letter])) {
            maxCounter = Math.max(maxCounter, counter)
            counter = i - letterToPosition[letter]
            for (const key in letterToPosition) {
                if (letterToPosition[key] <= letterToPosition[letter]) {
                    delete letterToPosition[key]
                }
            }
        } else {
            counter++
        }
        letterToPosition[letter] = i
    }

    return Math.max(counter, maxCounter)
}
