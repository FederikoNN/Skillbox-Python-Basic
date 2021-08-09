import timeit

res: float = timeit.timeit('"-".join(str(n) for n in range(100))', number=10000)
print(res)

res: float = timeit.timeit('"-".join([str(n) for n in range(100)])', number=10000)
print(res)

res: float = timeit.timeit('"-".join(map(lambda num: str(num), range(100)))', number=10000)
print(res)

# зачёт!
