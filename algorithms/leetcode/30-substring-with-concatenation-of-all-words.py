class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        if not s or not words:
            return []
        s_len, w_len = len(s), len(words[0])
        w_len_total = len(words) * w_len
        counter = {}
        for word in words:
            counter[word] = counter.get(word, 0) + 1
        curr = {}
        res = []
        for start in range(w_len):
            curr = {}
            end = start
            while start + w_len_total <= s_len:
                sub = s[end:end+w_len]
                end += w_len
                if sub not in counter:
                    curr = {}
                    start = end
                else:
                    curr[sub] = curr.get(sub, 0) + 1
                    while curr[sub] > counter[sub]:
                        curr[s[start: start+w_len]] -= 1
                        start += w_len
                    if start + w_len_total == end:
                        res.append(start)
        return res



if __name__ == '__main__':
    s = "barfoothefoobarman"
    words = ["foo", "bar"]
    print Solution().findSubstring(s, words)
