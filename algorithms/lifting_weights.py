# Roblox SWE Intern OA 2021, failed
# https://cdn.discordapp.com/attachments/321084536308105217/765736451362914304/6d20c583-a170-479a-9f62-7681ba81c997_1600719477.png

class Solution:
    def lifting_weights(weights, capacity):
        m = [[0]*(capacity+1) for _ in range(len(weights)+1)]
        for i in range(1, len(weights)+1):
            for j in range(1, capacity+1):
                if weights[i-1] > j:
                    m[i][j] = 0
                else:
                    m[i][j] = max(m[i-1][j], weights[i-1]+m[i-1][j-weights[i-1]])
        return m[-1][-1]
