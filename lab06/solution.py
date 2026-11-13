from pathlib import Path


def count_by_extension(paths: list[str]) -> dict[str, int]:
    counts = {}
    for path in paths:
        
        ext = Path(path).suffix.lower()
        
        if ext.startswith("."):
            ext = ext[1:]
        counts[ext] = counts.get(ext, 0) + 1
    return counts


def deepest_path(paths: list[str]) -> str:
    if not paths:
        return ""
    
    max_depth = max(p.count("/") for p in paths)
    
    deepest = [p for p in paths if p.count("/") == max_depth]
    
    return min(deepest)

def human_size(n_bytes: int) -> str:
    units = ["Б", "КБ", "МБ", "ГБ", "ТБ"]
    
    # Если меньше килобайта — выводим целое число байт
    if n_bytes < 1024:
        return f"{n_bytes} {units[0]}"
    
    # Для остальных единиц делим на 1024
    size = float(n_bytes)
    for unit in units[1:]:
        size /= 1024.0
        # Если после деления размер меньше 1024 или это последняя единица (ТБ)
        if size < 1024.0 or unit == units[-1]:
            return f"{size:.1f} {unit}"