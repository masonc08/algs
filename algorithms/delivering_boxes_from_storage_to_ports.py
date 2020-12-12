class Solution:
    def boxDelivering(self,
                      boxes: List[List[int]],
                      portsCount: int,
                      maxBoxes: int,
                      maxWeight: int) -> int:
        sol = 0
        for i, v in enumerate(boxes):
            dest, weight = v
