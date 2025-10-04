import os
import pandas as pd
import mimetypes

def describe_file(path: str):
    if os.path.isdir(path):
        return describe_folder(path)

    info = {
        "name": os.path.basename(path),
        "size_kb": round(os.path.getsize(path) / 1024, 2),
        "type": mimetypes.guess_type(path)[0] or "unknown"
    }

    # Simple CSV summary
    if path.endswith(".csv"):
        try:
            df = pd.read_csv(path, nrows=100)
            info["columns"] = list(df.columns)
            info["rows_estimate"] = sum(1 for _ in open(path)) - 1
        except Exception as e:
            info["error"] = f"CSV parse failed: {e}"

    # Simple TXT summary
    elif path.endswith(".txt") or path.endswith(".md"):
        try:
            with open(path, "r", encoding="utf-8", errors="ignore") as f:
                lines = f.readlines()
            info["line_count"] = len(lines)
            info["preview"] = "".join(lines[:5])
        except:
            pass

    return info

def describe_folder(path: str):
    summary = {"total_files": 0, "by_extension": {}}
    for root, _, files in os.walk(path):
        for f in files:
            summary["total_files"] += 1
            ext = os.path.splitext(f)[-1].lower() or "no_ext"
            summary["by_extension"][ext] = summary["by_extension"].get(ext, 0) + 1
    return summary
