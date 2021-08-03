import random


def ranking():
    rank = random.randint(1, 26)
    return rank


if __name__ == '__main__':
    print("GT is ranked number {} in the nation!".format(ranking()))
