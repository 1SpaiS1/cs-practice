import json
import csv
import io


def csv_to_records(text: str) -> list[dict]:
    if not text.strip():
        return []
    
    
    f = io.StringIO(text.strip())
    reader = csv.DictReader(f)
    
    records = []
    for row in reader:
        
        clean_row = {k.strip(): v.strip() for k, v in row.items() if k is not None}
        records.append(clean_row)
    return records


def records_to_json(records: list[dict]) -> str:
    
    return json.dumps(records, ensure_ascii=False, indent=2, sort_keys=True)