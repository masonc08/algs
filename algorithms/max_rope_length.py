"""
https://cdn.discordapp.com/attachments/321084536308105217/769374570581852160/unknown.png
"""


class Solution:
    def max_rope_length(self, lengths, segments):
        segment = max(lengths)
        i = 0
        j = segment
        while i <= j:
            mid = (i+j)/2
            possible_segments = self.get_segments(mid, lengths)
            if possible_segments < segments:
                if j == mid:
                    break
                j = mid
            else:
                if i == mid:
                    break
                i = mid
        return (i+j)/2
            

    def get_segments(self, length, segments):
        sol = 0
        for segment in segments:
            sol += segment//length
        return sol

print(Solution().max_rope_length([802, 743, 457, 539], 11))
