class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        if ay1 <= by1 <= ay2 <= by2:
            cy1, cy2 = by1, ay2
        elif by1 <= ay1 <= by2 <= ay2:
            cy1, cy2 = ay1, by2
        elif ay1 <= by1 <= by2 <= ay2:
            cy1, cy2 = by1, by2
        elif by1 <= ay1 <= ay2 <= by2:
            cy1, cy2 = ay1, ay2
        else:
            cy1, cy2 = 0, 0
        if ax1 <= bx1 <= ax2 <= bx2:
            cx1, cx2 = bx1, ax2
        elif bx1 <= ax1 <= bx2 <= ax2:
            cx1, cx2 = ax1, bx2
        elif ax1 <= bx1 <= bx2 <= ax2:
            cx1, cx2 = bx1, bx2
        elif bx1 <= ax1 <= ax2 <= bx2:
            cx1, cx2 = ax1, ax2
        else:
            cx1, cx2 = 0, 0
        return abs((ax2 - ax1)*(ay2 - ay1)) + abs((bx2 - bx1)*(by2 - by1)) - abs((cx2 - cx1)*(cy2 - cy1))