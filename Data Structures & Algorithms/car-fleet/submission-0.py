class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # time = (target - position) / speed
        # how do I use a stack for this
        cars = sorted(zip(position, speed), reverse=True)
        stack = []  # arrival times of each fleet

        for p, s in cars:
            time = (target - p) / s
            if not stack or time > stack[-1]:
                stack.append(time)  # can't catch the fleet ahead
            # else: catches up. merges, push nothing

        return len(stack)


