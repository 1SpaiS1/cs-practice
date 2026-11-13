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