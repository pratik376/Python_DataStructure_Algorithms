from typing import List


class Solution:
    def findStrobogrammatic(self, n: int) -> List[str]:

        res = []

        # valid left-right pairs
        pairs = [
            ("0", "0"),
            ("1", "1"),
            ("6", "9"),
            ("8", "8"),
            ("9", "6")
        ]

        path = [""] * n

        def dfs(left, right):

            # complete string
            if left > right:
                res.append("".join(path))
                return

            for a, b in pairs:

                # cannot start a multi-digit number with 0
                if left == 0 and n > 1 and a == "0":
                    continue

                # center position for odd n
                if left == right and a != b:
                    continue

                path[left] = a
                path[right] = b

                dfs(left + 1, right - 1)

        dfs(0, n - 1)

        return res