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

def _parse_value(val: str):
    
    low_val = val.lower()
    if low_val in ("true", "yes"):
        return True
    if low_val in ("false", "no"):
        return False
    
    # Пробуем целое число
    try:
        return int(val)
    except ValueError:
        pass
        
    
    try:
        return float(val) 
    except ValueError:
        pass
        
    
    return val


def parse_settings(lines: list[str]) -> dict:
    result = {}
    current_list_key = None
    
    for line in lines:
        
        line = line.split("#")[0].rstrip()
        if not line.strip():
            continue
            
        stripped = line.strip()
        
        
        if stripped.startswith("- "):
            if current_list_key is not None:
                val = stripped[2:].strip()
                result[current_list_key].append(_parse_value(val))
            continue
            
        
        if ":" in stripped:
            key, val = stripped.split(":", 1)
            key = key.strip()
            val = val.strip()
            
            if val:
                result[key] = _parse_value(val)
                current_list_key = None
            else:
                result[key] = []
                current_list_key = key
                
    return result


def merge_by_key(rows: list[dict], extra: dict, key: str = "id") -> list[dict]:
    result = []
    for row in rows:
        
        key_val = row.get(key)
        merged_row = {}
        
       
        if key_val in extra:
            merged_row.update(extra[key_val])
            
        
        merged_row.update(row)
        result.append(merged_row)
        
    return result