import itertools

def stylish(diff, replacer=' ', spaces_count=1):

    def iter_(current_value, depth):
        deep_indent = replacer * (depth)  # Отступ для вложенных элементов
        current_indent = replacer * (depth + spaces_count)   # Отступ для закрывающей скобки
        lines = []
        if not isinstance(current_value, dict):
            return str(current_value)
 
        for key, val in current_value.items():
            if isinstance(val, dict) and set(val.keys()) == {"-", "+"}:
                lines.append(f"{deep_indent}- {key}: {iter_(val['-'], depth + spaces_count)}")
                lines.append(f"{deep_indent}+ {key}: {iter_(val['+'], depth + spaces_count)}")
            elif isinstance(val, dict) and "+" in val:
                lines.append(f"{deep_indent}+ {key}: {iter_(val['+'], depth + spaces_count)}")
            elif isinstance(val, dict) and "-" in val:
                lines.append(f"{deep_indent}- {key}: {iter_(val['-'], depth + spaces_count)}")
            elif isinstance(val, dict):
                lines.append(f"{deep_indent}  {key}: {iter_(val, depth + spaces_count)}")
            else:
                lines.append(f"{deep_indent}  {key}: {iter_(val, depth)}")

#        for key, val in current_value.items():
#            lines.append(f'{deep_indent}{key}: {iter_(val, deep_indent_size)}')
        result = itertools.chain("{", lines, [current_indent + "}"])
#        result = ["{"]
#        result.extend(lines)
#        result.append(current_indent + "}")

        return '\n'.join(result)

    return iter_(diff, spaces_count)
