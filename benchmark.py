from timer import Timer
import random
LOOP_COUNT=1000000

with Timer(verbose=True) as t:
    data = (1,2,3,4,5,6,7,8,9,10)
    for c in range(LOOP_COUNT):
        hoge = random.choice(data)


with Timer(verbose=True) as u:
        fuga = random.randint(1,10)

pass