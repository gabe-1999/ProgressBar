import math

def progress_bar(progress, total):
    percent = 100 * (progress / float(total))
    total / 50 
    bar = "\u2588" * int((percent / 100) * 50) + "-" * (50 - int((percent / 100) * 50))
    print(f"\r|{bar}| {percent:.2f}", end="\r")
    if progress == total:
        print()

numbers = [x * 5 for x in range(3000, 5000)]
result = []

progress_bar(0, len(numbers))
for i, x in enumerate(numbers):
    progress_bar(i + 1, len(numbers))
    result.append(math.factorial(x))