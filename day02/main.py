from itertools import pairwise
from typing import Iterable

def are_numbers_increasing(vals: list[int]):
    return all(l < r and 1 <= r - l <= 3 for l, r in pairwise(vals))

def check_row(vals: list[int]):
    return are_numbers_increasing(vals) or are_numbers_increasing(vals[::-1])

def omit_one(vals: list[int]) -> Iterable[list[int]]:
    for idx in range(len(vals)):
        yield vals[:idx] + vals[idx + 1 :]

def parse_int(something):
    return [int(n) for n in something]

def check_reports(data: str):
    lines = [parse_int(r.split()) for r in data.strip().splitlines()]
    return sum(check_row(l) or any(check_row(o) for o in omit_one(l)) for l in lines)



