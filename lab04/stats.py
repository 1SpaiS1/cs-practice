def parse_record(line: str) -> dict:


    parts = line.split(";")
    if len(parts) != 3:
        raise ValueError(
            f"ожидалось 3 поля через ';', получено {len(parts)}: {line!r}"
        )

    city_raw, temp_raw, date_raw = parts


    city = city_raw.strip()
    date = date_raw.strip()


    if city == "":
        raise ValueError(f"пустое название города: {line!r}")
    if date == "":
        raise ValueError(f"пустая дата: {line!r}")


    temp_text = temp_raw.strip()
    try:
        temperature = float(temp_text)
    except ValueError:
        raise ValueError(
            f"температура не является числом: {temp_raw!r}"
        ) from None


    return {
        "city": city,
        "temperature": temperature,
        "date": date,
    }

def read_valid(lines: list[str]) -> list[dict]:

    records = []
    for line in lines:
       
        if line.strip() == "":
            continue

        
        try:
            records.append(parse_record(line))
        except ValueError:
            continue

    return records

