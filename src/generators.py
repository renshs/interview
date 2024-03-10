import src.constants as constants
from src.decorators import benchmark


@benchmark
def pairs_generator_fast(n: int = 5) -> None:
    """
    This functioin prints pairs of capital and lowercase english letters.
    Using one loop and slices.

    Variables:
        n: Number of pairs.
    """
    if not isinstance(n, int):
        raise TypeError(f"Argument shuld be int, given {type(n)}")
    if n < 0:
        raise ValueError(f"Argument should be more or equal to 0, given {n}")
    for i in range(1, n + 1):
        cnt_full_lines = i // 26
        print(constants.PAIRS * cnt_full_lines, end="")
        print(constants.PAIRS[: 2 * (i % 26)])


@benchmark
def pairs_generator_m_e(n: int = 5) -> None:
    """
    This function prints pairs of capital and lowercase english letters.
    This emplementation most memory efficient

    Variables:
        n: Number of pairs.
    """
    if not isinstance(n, int):
        raise TypeError(f"Argument shuld be int, given {type(n)}")
    if n < 0:
        raise ValueError(f"Argument should be more or equal to 0, given {n}")
    for i in range(1, n + 1):
        for letters in range(i):
            print(
                f"{chr(65 + (letters % 26))}{chr(97 + (letters % 26))}", end=""
            )
        print()


def pairs_generator_short(n: int = 5) -> None:
    """
    This function prints pairs of capital and lowercase english letters.
    This is the shortest version

    Variables:
        n: Number of pairs.
    """
    if not isinstance(n, int):
        raise TypeError(f"Argument shuld be int, given {type(n)}")
    if n < 0:
        raise ValueError(f"Argument should be more or equal to 0, given {n}")
    print("\n".join([constants.PAIRS*(i//26)+constants.PAIRS[:2*(i % 26)] for i in range(1, n + 1)]))
