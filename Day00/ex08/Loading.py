from tqdm import tqdm
import time
from time import sleep


def ft_tqdm(lst: range) -> None:
    x = 1
    b = '█'
    formed = ''
    transfered = 1
    max_len = len(lst)
    step = int(100 / max_len)
    print(100/66)
    for elem in lst:
        print(step)
        formed = f'{x}% |{((b*x)):<100}| {transfered}/{max_len}'
        x += step
        transfered += 1
        yield print(f'\r\33[K{formed}', end='')
    print(end='\n')


for elem in ft_tqdm(range(66)):
    sleep(0.5)
