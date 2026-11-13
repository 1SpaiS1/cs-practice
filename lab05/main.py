from logstats import count_levels, top_errors, format_report, parse_event


def main() -> None:
    filename = input().strip()

    total = errors = broken = 0
    with open(filename, encoding="utf-8") as log:
        for line in log:
            if not line.strip():
                continue
            total += 1
            try:
                event = parse_event(line)
            except ValueError:
                broken += 1
                continue
            if event["level"] == "ERROR":
                errors += 1
    print(total)
    print(errors)
    print(broken)

    with open(filename, encoding="utf-8") as log:
        counts = count_levels(log)
    with open(filename, encoding="utf-8") as log:
        top = top_errors(log, 3)

    with open("report.txt", "w", encoding="utf-8") as out:
        out.write(format_report(counts, top))


if __name__ == "__main__":
    main()