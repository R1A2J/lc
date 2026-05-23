class Solution:
    def encode(self, strs: List[str]) -> str:
        s, l = '', ''
        for i in strs:
            s += i + '\u0986'
        return s

    def decode(self, s: str) -> List[str]:
        answer = []
        start = 0
        for i in range(len(s)):
            if s[i] == '\u0986':
                answer.append(s[start:i])
                start = i + 1
        return answer
