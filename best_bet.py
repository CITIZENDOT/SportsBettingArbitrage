import re


MAX_CAPITAL = 50
INT_OR_FLOAT = re.compile(r"^-?\d*(\.(\d?)*)?$")


def find_combinations(total: int, m: int, current=[]):
    if m == 0:
        if total == 0:
            yield current
        return

    for i in range(0, total + 1):
        yield from find_combinations(total - i, m - 1, current + [i])


def calculate_expected_value(bets, _choices, combinations):
    choices = _choices.copy()
    n, m = len(bets), len(bets[0])
    expected_values = []
    for comb in combinations:
        entry = {"choices": choices, "division": comb, "winnings": []}
        for i in range(m):
            # If ith choice is won, calculate the winnings
            winnings = 0
            for j, bookmaker_index in enumerate(choices):
                winnings -= comb[j]  # Deduct the amount betted
                if j == i:
                    winnings += comb[j] * bets[bookmaker_index][j]

            entry["winnings"].append(winnings)

        expected_values.append(entry)

    return expected_values


def calculate_expected_value_recursive(
    bets, combinations, current=[], expected_values=[]
):
    n, m = len(bets), len(bets[0])
    if len(current) == m:
        curr_expected_values = calculate_expected_value(bets, current, combinations)
        expected_values.extend(curr_expected_values)
        return

    for bookmaker_index in range(n):
        current.append(bookmaker_index)
        calculate_expected_value_recursive(bets, combinations, current, expected_values)
        current.pop()


def get_input():
    bets = []
    labels = []
    m = -1
    bookmarker_index = 0
    while True:
        try:
            line = input()
            if line == "":
                break
            line = line.strip().split()
            label = f"Bookmaker {bookmarker_index + 1}"
            if INT_OR_FLOAT.match(line[-1]):
                current_choices_count = len(line)
            else:
                current_choices_count = len(line) - 1
                label = line[-1]

            if m == -1:
                m = current_choices_count
            else:
                if m != current_choices_count:
                    raise ValueError("Invalid input")

            current_choices = []
            for i in range(current_choices_count):
                current_choices.append(float(line[i]))

            bets.append(current_choices)
            labels.append(label)

            bookmarker_index += 1

        except EOFError:
            break

    return bets, labels


def main():
    bets, labels = get_input()
    n, m = len(bets), len(bets[0])

    combinations = list(find_combinations(MAX_CAPITAL, m))

    expected_values = []
    calculate_expected_value_recursive(bets, combinations, [], expected_values)
    zero_risk_bets = [x for x in expected_values if all(y >= 0 for y in x["winnings"])]
    if len(zero_risk_bets) == 0:
        print("No zero risk bets")
        return

    zero_risk_bets.sort(key=lambda x: sum(x["winnings"]) / m, reverse=True)
    print("Zero risk bets:")
    print("---------------\n")

    for i, bet in enumerate(zero_risk_bets):
        print(f"Bet {i + 1}:")
        for event in range(m):
            bookkeeper_index = bet["choices"][event]
            stake = bet["division"][event]
            bookkeeper_label = labels[bookkeeper_index]
            # current_odds = bets[bookkeeper_index][event]
            print(f"\tStake ${stake} on event {event + 1} with {bookkeeper_label}.")
        print(f"\n\tWinnings:")
        for j, winnings in enumerate(bet["winnings"]):
            print(f"\t\tIf event {j + 1}: Profit: ${round(winnings, 2)}")

        print()


if __name__ == "__main__":
    main()
