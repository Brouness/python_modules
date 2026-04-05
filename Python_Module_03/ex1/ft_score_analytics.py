import sys


def main() -> None:
    print("=== Player Score Analytics ===")
    if len(sys.argv) == 1:
        print("No scores provided. Usage: python3 "
              + "ft_score_analytics.py <score1> <score2> ...")
        return
    scores = []
    for i in sys.argv[1:]:
        try:
            a = int(i)
            scores.append(a)
        except ValueError:
            print(f"Invalid parameter: '{i}'")
    if len(scores) == 0:
        print("No scores provided. Usage: python3 "
              + "ft_score_analytics.py <score1> <score2> ...")
        return
    else:
        print(f"Scores processed: {scores}")
        print(f"Total players: {len(scores)}")
        print(f"Total score: {sum(scores)}")
        print(f"Average score: {sum(scores) / len(scores)}")
        print(f"High score: {max(scores)}")
        print(f"Low score: {min(scores)}")
        print(f"Score range: {max(scores) - min(scores)}")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Caught Uknown Error: {e}")
    print()
