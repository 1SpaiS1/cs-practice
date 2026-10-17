

import sys

from stats import average_by_city, read_valid, warmest_city


def main() -> None:
    
    lines = sys.stdin.read().splitlines()

    
    valid = read_valid(lines)

    
    non_empty = [line for line in lines if line.strip() != ""]
    skipped = len(non_empty) - len(valid)

    
    averages = average_by_city(valid)
    best = warmest_city(valid)

    
    print(len(valid))
    print(skipped)

    
    if best == "":
        print("0.0")
    else:
        print(f"{averages[best]:.1f}")


if __name__ == "__main__":
    main()
