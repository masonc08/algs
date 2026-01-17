from typing import List

class Solution:
    def bestTower(self, towers: List[List[int]], center: List[int], radius: int) -> List[int]:
        best_tower = None
        x0, y0 = center
        for x, y, h in towers:
            cur_distance = abs(x-x0)+abs(y-y0)
            if cur_distance > radius:
                continue
            if best_tower is None or h > best_tower[2]:
                best_tower = x, y, h
            elif h == best_tower[2]:
                best_tower = min(
                    [x, y, h],
                    best_tower,
                    key=lambda x:(x[0], x[1]),
                )
        return best_tower[:2] if best_tower is not None else [-1, -1]
    