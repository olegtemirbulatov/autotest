import random
import time


class LoopsPractice:

    def print_numbers_list():
        numbers = list(range(1, 8))
        for n in numbers:
            print(n)
            if n == 5:
                break

    def print_strings_list():
        words = [f"str{i}" for i in range(10)]
        for w in words:
            print(w)


class RosticsLoadImitation:

    def imitate_load():
        it = 0
        while it < 10:
            if random.randint(0, 100) > 85:
                print("Warning! Load > 85%")
            time.sleep(0.2)
            it += 1


LoopsPractice.print_numbers_list()
LoopsPractice.print_strings_list()
RosticsLoadImitation.imitate_load()
