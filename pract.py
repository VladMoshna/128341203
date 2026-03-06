# zavd 1
def power(a, n):
    if n == 0:
        return 1
    return a * power(a, n - 1)


# zavd 2
def days_diff(d1, m1, y1, d2, m2, y2):

    def leap(y):
        return (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0)

    def date_to_days(d, m, y):
        months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        days = d

        for year in range(1, y):
            days += 366 if leap(year) else 365

        for month in range(1, m):
            if month == 2 and leap(y):
                days += 29
            else:
                days += months[month - 1]

        return days

    return abs(date_to_days(d1, m1, y1) - date_to_days(d2, m2, y2))


# zavd 3
import random

def find_min(arr, i=0, best_i=0, best_sum=None):
    if i > len(arr) - 10:
        return best_i
    s = sum(arr[i:i+10])
    if best_sum is None or s < best_sum:
        return find_min(arr, i + 1, i, s)
    return find_min(arr, i + 1, best_i, best_sum)


nums = [random.randint(-100, 100) for _ in range(100)]

print(power(2, 5))
print(days_diff(1, 1, 2020, 1, 1, 2021))
print(find_min(nums))