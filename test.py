import math

def progress_bar(progress, total):
    percent = 100 * (progress / float(total))
    bar = "\u2588" * int(percent) + "-" * (100 - int(percent))
    print(f"\r|{bar}| {percent:.2f}", end="\r")

numbers = [x * 5 for x in range(3000, 5000)]
result = []

progress_bar(0, len(numbers))
for i, x in enumerate(numbers):
    progress_bar(i + 1, len(numbers))
    math.factorial(x)