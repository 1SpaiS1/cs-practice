LEVELS = {"DEBUG", "INFO", "WARNING", "ERROR"}


def parse_event(line: str) -> dict:
    parts = line.strip().split(maxsplit=2)
    if len(parts) != 3:
        raise ValueError(f"bad line: {line!r}")
    time, level, message = parts
    if level not in LEVELS:
        raise ValueError(f"bad level: {level!r}")
    return {"time": time, "level": level, "message": message}


def count_levels(lines) -> dict:
    counts: dict = {}
    for line in lines:
        if not line.strip():
            continue
        try:
            event = parse_event(line)
        except ValueError:
            counts["BROKEN"] = counts.get("BROKEN", 0) + 1
            continue
        level = event["level"]
        counts[level] = counts.get(level, 0) + 1
    return counts


def top_errors(lines, n: int) -> list:
    counter: dict = {}
    for line in lines:
        if not line.strip():
            continue
        try:
            event = parse_event(line)
        except ValueError:
            continue
        if event["level"] == "ERROR":
            msg = event["message"]
            counter[msg] = counter.get(msg, 0) + 1
    items = sorted(counter.items(), key=lambda kv: (-kv[1], kv[0]))
    return [[msg, cnt] for msg, cnt in items[:n]]


def format_report(counts: dict, errors: list) -> str:
    lines = ["Отчёт по журналу", ""]
    for level in sorted(counts):
        lines.append(f"{level}: {counts[level]}")
    lines.append("")
    lines.append("Частые ошибки:")
    for msg, cnt in errors:
        lines.append(f"- {msg} — {cnt}")
    return "\n".join(lines) + "\n"