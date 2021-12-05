import collections


class Solution:
    def validArrangement(self, pairs: List[List[int]]) -> List[List[int]]:
        mp = collections.defaultdict(set)
        mp2 = collections.defaultdict(int)
        for pair in pairs:
            mp[pair[0]].add(tuple(pair))
            mp2[pair[0]] += 1
            mp2[pair[1]] -= 1
            if mp2[pair[1]] == 0:
                del mp2[pair[1]]
            if mp2[pair[0]] == 0:
                del mp2[pair[0]]
        sol = []
        def recurse(end):
            if len(sol) == len(pairs):
                return True
            for pair in mp[end]:
                sol.append(list(pair))
                mp[end].remove(pair)
                if recurse(pair[1]):
                    return True
                mp[end].add(pair)
                sol.pop()
            return False
        if mp2:
            for k, v in mp2.items():
                if v == 1:
                    for pair in mp[k]:
                        sol.append(pair)
                        mp[pair[0]].remove(pair)
                        if recurse(pair[1]):
                            return sol
                        mp[pair[0]].add(pair)
                        sol.pop()
        else:
            pair = pairs[0]
            sol.append(pair)
            mp[pair[0]].remove(tuple(pair))
            if recurse(pair[1]):
                return sol
            mp[pair[0]].add(tuple(pair))
            sol.pop()
        raise Exception()


# import collections


# class Solution:
#     def validArrangement(self, pairs: List[List[int]]) -> List[List[int]]:
#         mp = collections.defaultdict(list)
#         mp2 = collections.defaultdict(int)
#         for pair in pairs:
#             mp[pair[0]].append(tuple(pair))
#             mp2[pair[0]] += 1
#             mp2[pair[1]] -= 1
#             if mp2[pair[1]] == 0:
#                 del mp2[pair[1]]
#             if mp2[pair[0]] == 0:
#                 del mp2[pair[0]]
#         sol = []
#         occupied = set()
#         def recurse(end):
#             if len(sol) == len(pairs):
#                 return True
#             for pair in mp[end]:
#                 if tuple(pair) in occupied:
#                     continue
#                 sol.append(pair)
#                 occupied.add(tuple(pair))
#                 if recurse(pair[1]):
#                     return True
#                 occupied.remove(tuple(pair))
#                 sol.pop()
#             return False
#         if mp2:
#             for k, v in mp2.items():
#                 if v == 1:
#                     for pair in mp[k]:
#                         occupied.add(tuple(pair))
#                         sol.append(pair)
#                         if recurse(pair[1]):
#                             return sol
#                         sol.pop()
#                         occupied.remove(tuple(pair))
#         else:
#             for pair in pairs:
#                 occupied.add(tuple(pair))
#                 sol.append(pair)
#                 if recurse(pair[1]):
#                     return sol
#                 sol.pop()
#                 occupied.remove(tuple(pair))
#         raise Exception()
