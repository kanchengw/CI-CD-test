from collections import defaultdict
from typing import List

def dedupe_header(columns: List[str]) -> List[str]:
    """
    Make header column names unique by appending numeric suffixes to duplicates, ignoring case by default.
    Rules:
    - The first occurrence of a name (case-insensitive) is kept as-is.
    - The 2nd, 3rd, ... occurrences of the same name (case-insensitive) get ".1", ".2", ...appended.
    - Order is preserved exactly as given.
    - Input is a list of strings (column names); output is a same-length list.
    Example:
    ["id", "ID", "Id", "name", "NAME"] -> ["id", "id.1", "id.2", "name", "name.1"]
    """
    seen_counts = defaultdict(int)
    result: List[str] = []
    for col in columns:
        # 转为小写，实现忽略大小写
        lower_col = col.lower()
        count = seen_counts[lower_col]
        if count == 0:
            result.append(col)
        else:
            result.append(f"{col}.{count}")
        seen_counts[lower_col] += 1
    return result