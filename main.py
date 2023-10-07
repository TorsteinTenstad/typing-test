import numpy as np
import time

if __name__ == '__main__':
    while 1:
        symbols = "|@#$%/[]=\!\",.&{()}?';:*_-+<>]"
        symbols = np.array([s for s in symbols])
        word = np.random.choice(symbols, 20)
        word = ''.join(word)
        input("Press enter to start")
        print(word + '\n')
        start_time = time.time()
        answer = input()
        end_time = time.time()
        accuracy = np.average([1 if a==s else 0 for (a, s) in zip(word,list(answer)+[' ']*(len(word)-len(answer)))])
        print(f"time: {end_time - start_time:.2f}s, accuracy: {100*accuracy:.0f}%")
        with open('stats.txt', 'a') as f:
            f.write(f"{end_time - start_time:.2f},{100*accuracy:.0f}\n")