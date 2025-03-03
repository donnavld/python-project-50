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
 
def format_value(value):
    """Форматирует значение для вывода в plain-формате."""
    if isinstance(value, dict):
        return "[complex value]"
    if isinstance(value, str):
        return f"'{value}'"
    return str(value).lower()  # Для bool и None

def plain(diff):
    def iter_(current_value, path=""):
        lines = []

        for key, val in sorted(current_value.items()):
            new_path = f"{path}.{key}" if path else key

            if isinstance(val, dict) and set(val.keys()) == {"-", "+"}:
                lines.append(f"Property '{new_path}' was updated. From {format_value(val['-'])} to {format_value(val['+'])}")
            elif isinstance(val, dict) and "+" in val:
                lines.append(f"Property '{new_path}' was added with value: {format_value(val['+'])}")
            elif isinstance(val, dict) and "-" in val:
                lines.append(f"Property '{new_path}' was removed")
            elif isinstance(val, dict):
                lines.append(iter_(val, new_path))  # Рекурсивно углубляемся

        return '\n'.join(filter(None, lines))  # Убираем пустые строки

    return iter_(diff)

