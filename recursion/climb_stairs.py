class Solution:
    def climbStairs(self, n: int) -> int:
        cache = {}

        def steps(n):
            if n in cache:
                return cache[n]

            if n <= 2:
                result = n
            else:
                result = steps(n - 1) + steps(n - 2)

            cache[n] = result
            return result

        return steps(n)


if __name__ == "__main__":
    solution = Solution()

    for number_of_stairs in range(1, 6):
        print(number_of_stairs, solution.climbStairs(number_of_stairs))
