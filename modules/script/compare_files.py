def diff_dicts(d1, d2):
    result = []
    keys1 = set(d1.keys())
    keys2 = set(d2.keys())
    for key in sorted(keys1 & keys2):
        if d1[key] != d2[key]:
            result.append(f"- {key}: {d1[key]}")
            result.append(f"+ {key}: {d2[key]}")
        else:
            # Если значения совпадают, можно не выводить или выводить без знака
            result.append(f"  {key}: {d1[key]}")
    
    # Ключи, которые есть только в d1 (удалены)
    for key in sorted(keys1 - keys2):
        result.append(f"- {key}: {d1[key]}")
    
    # Ключи, которые есть только в d2 (добавлены)
    for key in sorted(keys2 - keys1):
        result.append(f"+ {key}: {d2[key]}")
        
    return "\n".join(result)
