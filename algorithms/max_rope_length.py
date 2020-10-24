"""
https://cdn.discordapp.com/attachments/321084536308105217/769374570581852160/unknown.png
Doesn't work perfectly
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
                j = mid - 1
            else:
                i = mid + 1
        return j
            

    def get_segments(self, length, segments):
        sol = 0
        for segment in segments:
            sol += segment//length
        return sol

print(Solution().max_rope_length([802, 743, 457, 539], 11))
