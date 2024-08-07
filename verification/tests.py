"""
TESTS is a dict with all of your tests.
Keys for this will be the categories' names.
Each test is a dict with
    "input" -- input data for a user function
    "answer" -- your right answer
    "explanation" -- not necessarily a key, it's used for an additional info in animation.
"""

def shell_game(shell: str, moves: list[int]) -> str:

    table = {x: 0 for x in "ABC"}
    table[shell] = 1
    for move in moves:
        match move:
            case 1: table["A"], table["B"] = table["B"], table["A"]
            case 2: table["C"], table["B"] = table["B"], table["C"]
            case 3: table["A"], table["C"] = table["C"], table["A"]

    return next(x for x in table if table[x])

from random import randint

def generate():

    shell = "ABC"[randint(0, 2)]
    num_moves = randint(1, 10)
    moves = [randint(1, 3) for _ in range(num_moves)]

    return [shell, moves]

rand = []
for _ in range(12):
   case = {}
   s, m = generate()
   case["input"] = [s, m]
   case["answer"] = shell_game(s, m)
   rand.append(case)

TESTS = {
    "Basics": [
            {
        "input": ['A', [1, 2, 3]],
        "answer": "A",
    },
    {
        "input": ['C', [1, 2, 3, 3, 1, 1]],
        "answer": "B",
    },
    {
        "input": ['B', [3]],
        "answer": "B",
    },
    {
        "input": ['B', []],
        "answer": "B",
    },
    ], 
    "Random": rand,
}
