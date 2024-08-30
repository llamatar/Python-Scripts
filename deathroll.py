"""
deathroll.py

I was introduced to a new "game" played on Discord by some folks at tabletop.
Two players roll a die where the maximum number is the previously rolled number.
You lose if you roll a 1.

I'm not really sure what's so fun about this "game", but because they were manually
changing the die maximum, I figured it would be trivial to do it in code.
"""

import random

DEFAULT_N = 100
DEFAULT_START_NUM = 10000


def main() -> None:
    # deathroll()
    # deathrolls(10)
    # calc_stats(deathrolls(10))
    # calc_stats(deathrolls(10000000, 10000, False))
    # deathroll_input()
    deathroll(start_num=DEFAULT_START_NUM, print_flag=True, wait_flag=False)


def deathroll(
    start_num: int = DEFAULT_START_NUM,
    print_flag: bool = False,
    wait_flag: bool = False,
) -> (int, int, []):
    """Repeatedly rolls random numbers capped at the previous random number until 1 is rolled. Returns (total number of rolls, winner, and list of rolls)."""
    random_num = start_num
    roll_count = 0
    rolls = []

    if print_flag:
        print(f"Deathroll starting from {start_num}")

    while random_num > 1:
        if wait_flag:
            input()

        roll_count += 1

        random_num = random.randint(1, random_num)
        rolls.append(random_num)

        if print_flag:
            print(
                f"[{roll_count}] Player {2 - (roll_count % 2)}: {random_num} ({random_num - start_num if len(rolls) == 1 else random_num - rolls[-2]}, {100 / random_num:.2f}%)",
                end=("" if wait_flag else "\n"),
            )

    winner = roll_count % 2 + 1

    if wait_flag:
        print()
    if print_flag:
        print(f"Player {winner} wins!\n")

    return (roll_count, winner, rolls)


def deathrolls(
    n: int = DEFAULT_N, start_num: int = DEFAULT_START_NUM, print_flag: bool = False
) -> [(int, int, [])]:
    """Runs n deathrolls. Returns a list of the results."""
    return [deathroll(start_num, print_flag) for _ in range(n)]


def calc_stats(deathrolls: [(int, int, [])]) -> None:
    """Prints stats about the given deathrolls."""
    roll_count_list = []
    winner_list = []
    rolls_list = []

    for roll_count, winner, rolls in deathrolls:
        roll_count_list.append(roll_count)
        winner_list.append(winner)
        rolls_list.append(rolls)

    len_rolls = len(roll_count_list)
    max_rolls = max(roll_count_list)
    min_rolls = min(roll_count_list)
    sum_rolls = sum(roll_count_list)
    avg_rolls = sum_rolls / len_rolls

    print(f"Deathrolls: {len_rolls}")
    print(f"Max rolls: {max_rolls}")
    print(f"Min rolls: {min_rolls}")
    print(f"Total rolls: {sum_rolls}")
    print(f"Average rolls: {avg_rolls}")
    print()

    player1_wins = winner_list.count(1)
    player2_wins = winner_list.count(2)

    print(f"Player 1 wins: {player1_wins} ({(player1_wins / len_rolls * 100):.2f}%)")
    print(f"Player 2 wins: {player2_wins} ({(player2_wins / len_rolls * 100):.2f}%)")
    print()

    max_win_streak, max_streak_winner = find_max_win_streak(winner_list)

    print(f"Max win streak: {max_win_streak} (won by Player {max_streak_winner})")
    print()

    longest_deathroll = next(rolls for rolls in rolls_list if len(rolls) == max_rolls)
    print(
        f"Longest deathroll ({max_rolls}): {longest_deathroll} (won by Player {max_rolls % 2 + 1})"
    )

    print()


def find_max_win_streak(winner_list: [int]) -> (int, int):
    """Returns the longest win streak and that streak's winner of the given list."""
    max_win_streak = 0
    max_streak_winner = None

    win_streak = 0
    streak_winner = None

    for winner in winner_list:
        if winner == streak_winner:
            win_streak += 1
            continue

        if win_streak > max_win_streak:
            max_win_streak = win_streak
            max_streak_winner = streak_winner

        win_streak = 1
        streak_winner = winner

    return (max_win_streak, max_streak_winner)


def deathroll_input() -> None:
    """Runs deathrolls according to input."""
    n = input(f"n [{DEFAULT_N}]: ")
    n = DEFAULT_N if len(n) == 0 else int(n)

    start_num = input(f"start_num [{DEFAULT_START_NUM}]: ")
    start_num = DEFAULT_START_NUM if len(start_num) == 0 else int(start_num)

    print()

    calc_stats(deathrolls(n, start_num, False))


if __name__ == "__main__":
    main()
