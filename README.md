# Arbitrage Betting (Sports)

Arbitrage betting is all about locking in a win -- or at least avoiding a loss—by betting on all possible outcomes of a sporting event with different bookmakers. The trick? Taking advantage of differences in the odds they offer. While guaranteed profit isn’t always possible, it's possible to avoid losing money (always!!).

A more comprehensive explanation of this concept can be found here: <https://youtu.be/2kDTwP6SBx4?si=EWr2y3ggOkbrHiki>

## How Sports betting Works

Here's a quick example. Say a bookmaker offers the following odds for a soccer match (let's not worry about draw for now):

- **Team A:** 1.9
- **Team B:** 1.8

It means:

- If you bet **\$1 on team A**, you will get **\$1.9** if team A wins. Net profit in this case is **\$0.9**.
- If you bet **\$1 on team B**, you will get **\$1.8** if team B wins. Net profit in this case is **\$0.8**.
- But If you bet on both teams, you’ll lose no matter what. Let's see why.
  - **If Team A wins:** You get \$1.9, but lose \$1 → Net loss = -\$0.10.
  - **If Team B wins:** You get \$1.8, but lose \$1 → Net loss = -\$0.20.

## Arbitrage Betting

Now, let’s add a second bookmaker:

|               | Team A | Team B |
| ------------- | ------ | ------ |
| Book keeper 1 | 1.9    | 1.8    |
| Book keeper 2 | 1.4    | 2.5    |

Arbitrage time! Bet **\$6 on Team A** (Book 1) and **\$4 on Team B** (Book 2):

- **If Team A wins:** \$6 × 1.9 = \$11.4. Subtract \$6 + \$4 → Profit = **\$1.40**.
- **If Team B wins:** \$4 × 2.5 = \$10. Subtract \$6 + \$4 → Profit = **\$0.00**.
  You’re guaranteed at least a break-even, and possibly a profit, but most importanly, not making a loss. Not bad, right?

## Arbitrage Betting Calculator

This script in this repository helps you find arbitrage opportunities and calculates how much to bet on each outcome. It works for events with two or more outcomes (e.g., win/lose, win/draw/lose). Just input odds, and it does the math for you.

## How to Use It

1. Enter the odds for all outcomes and, optionally, bookmaker names.
   - If no names? Default names like "_Bookmaker 1_" are assigned.
2. Cover all outcomes for all book-makers in the input:
   - If you don’t, the script will tell you (errors out).
3. Set your capital:

   - Default is **\$50**. Change it by tweaking the `MAX_CAPITAL` variable in the script.

```text
❯ python3 best_bet.py
1.9 1.8 SportsBet
1.4 2.5 Ladbrokes

Zero risk bets:
---------------

Bet 1:
        Stake $27 on event 1 with SportsBet.
        Stake $23 on event 2 with Ladbrokes.

        Winnings:
                If event 1: Profit: $1.3
                If event 2: Profit: $7.5

Bet 2:
        Stake $28 on event 1 with SportsBet.
        Stake $22 on event 2 with Ladbrokes.

        Winnings:
                If event 1: Profit: $3.2
                If event 2: Profit: $5.0

Bet 3:
        Stake $29 on event 1 with SportsBet.
        Stake $21 on event 2 with Ladbrokes.

        Winnings:
                If event 1: Profit: $5.1
                If event 2: Profit: $2.5

Bet 4:
        Stake $30 on event 1 with SportsBet.
        Stake $20 on event 2 with Ladbrokes.

        Winnings:
                If event 1: Profit: $7.0
                If event 2: Profit: $0.0
```
