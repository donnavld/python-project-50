from .stylish import stylish

def diff_plain_dicts(d1, d2):
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


def generate_diff_old(d1, d2, format_name='stylish'):

    def iner_dic(dic1, dic2):
        result = {}
        keys1 = set(dic1.keys())
        keys2 = set(dic2.keys())
        for key in sorted(keys1 & keys2):
            if isinstance(dic1[key], dict) and isinstance(dic2[key], dict):
                # Оба значения — словари, рекурсивно обрабатываем
                result[key] = iner_dic(dic1[key], dic2[key])
            else:
            # Если значения совпадают, можно не выводить или выводить без знака
                if dic1[key] != dic2[key]:
                    result[f"- {key}"] = dic1[key]
                    result[f"+ {key}"] = dic2[key]
                else:
                    result[key] = dic1[key]
        # Ключи, которые есть только в d1 (удалены)
        for key in sorted(keys1 - keys2):
            result[f"- {key}"] = dic1[key]
    
        # Ключи, которые есть только в d2 (добавлены)
        for key in sorted(keys2 - keys1):
            result[f"+ {key}"] = dic2[key]
        
        if format_name == 'stylish':
            return stylish(result)
        else:
            return result
    
    return iner_dic(d1,d2)


def generate_diff(d1, d2, format_name='stylish'):

    def iner_dic(dic1, dic2):
        result = {}
        keys1 = set(dic1.keys())
        keys2 = set(dic2.keys())
        for key in sorted(keys1 & keys2):
            if isinstance(dic1[key], dict) and isinstance(dic2[key], dict):
                # Оба значения — словари, рекурсивно обрабатываем
                result[key] = iner_dic(dic1[key], dic2[key])
            else:
            # Если значения совпадают, можно не выводить или выводить без знака
                if dic1[key] != dic2[key]:
                    result[key] = {"-": dic1[key], "+": dic2[key]}
                else:
                    result[key] = dic1[key]
        # Ключи, которые есть только в d1 (удалены)
        for key in sorted(keys1 - keys2):
            result[key] = {"-": dic1[key]} 
    
        # Ключи, которые есть только в d2 (добавлены)
        for key in sorted(keys2 - keys1):
            result[key] = {"+": dic2[key]} 
        
        return result
    
    return iner_dic(d1,d2)

