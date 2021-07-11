import { lengthOfLongestSubstring } from './longest_substring_without_repeating_characters'

test('test', () => {
    expect(lengthOfLongestSubstring('abcabcbb')).toBe(3)
    expect(lengthOfLongestSubstring('bbbbbb')).toBe(1)
    expect(lengthOfLongestSubstring('pwwkew')).toBe(3)
    expect(lengthOfLongestSubstring('')).toBe(0)
    expect(lengthOfLongestSubstring(' ')).toBe(1)
    expect(lengthOfLongestSubstring('dvdf')).toBe(3)
    expect(lengthOfLongestSubstring('cdd')).toBe(2)
    expect(lengthOfLongestSubstring('abba')).toBe(2)
})
