import argparse
from .script.get_file_extension import get_extension 
from .script.compare_files import generate_diff_get_result
from .script.stylish import stylish
from .script.load_file import load_file

from .script.get_print import stylish, plain, print_json

def generate_diff(d1, d2, format_name='stylish'):
    get_print = {"stylish": stylish, "plain": plain, "json": print_json}
#    print(d1)
    diff = generate_diff_get_result(d1,d2)
    if format_name in get_print:
        return get_print[format_name](diff)
    raise ValueError(f"Unsupported file format: {format_name}")

def diff_dict(d1, d2):
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

def main():
#    print("Hello from python-project-50!")
    parser = argparse.ArgumentParser(
                    prog='hexlet-code',
                    description='Compares two configuration files and shows a difference.',
                    epilog='Enter 2 foles')
    parser.add_argument("first_file", help="")
    parser.add_argument("second_file", help="")
#    parser.add_argument(
#        '-f','--format',
#        help='set format of output',
#        choices=['yaml', 'json'],
#        default='json'
#        ) 

    parser.add_argument(
        '-f', '--format',
        help='Output format (default: "stylish")',
        choices=['stylish', 'plain', 'json'],
        default='stylish'
    )

    parser.add_argument(
        '-V', '--version',
        help='Output the version number',
        action='version',
        version='gendiff 1.0.0'
    )

    args = parser.parse_args()

    dic_file1 = load_file(__file__, args.first_file)
    dic_file2 = load_file(__file__, args.second_file)
    
    result = generate_diff(dic_file1, dic_file2, format_name=args.format)
    print(result)
#    print(stylish(result))


if __name__ == "__main__":
    main()


