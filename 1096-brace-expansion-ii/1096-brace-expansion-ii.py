class Solution:
    def braceExpansionII(self, expression: str) -> list[str]:
        i = 0

        def parse():
            nonlocal i

            # res = union of completed comma-separated parts
            res = set()

            # cur = current concatenation result
            cur = {""}

            while i < len(expression) and expression[i] != "}":
                if expression[i] == ",":
                    res |= cur
                    cur = {""}
                    i += 1

                elif expression[i] == "{":
                    i += 1  # skip {
                    nxt = parse()
                    i += 1  # skip }

                    cur = {a + b for a in cur for b in nxt}

                else:
                    # Read consecutive letters
                    start = i
                    while i < len(expression) and expression[i].isalpha():
                        i += 1

                    word = expression[start:i]
                    cur = {a + word for a in cur}

            return res | cur

        return sorted(parse())