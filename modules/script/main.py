import argparse
import json
import os

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


def main():
    print("Hello from python-project-50!")
    parser = argparse.ArgumentParser(
                    prog='hexlet-code',
                    description='Compares two configuration files and shows a difference.',
                    epilog='Enter 2 foles')
    parser.add_argument("first_file", help="")
    #Compares two configuration files and shows a difference.
    parser.add_argument("second_file", help="")
    #Path to the second configuration file
    parser.add_argument(
        '-f','--format',
        help='set format of output',
        choices=['plain', 'json'],
        default='json'
        ) 
    args = parser.parse_args()
#    base_dir = "./files/"
    base_dir = os.path.join(os.path.dirname(__file__), "..", "files")
    first_file_path = os.path.join(base_dir, args.first_file)
    second_file_path = os.path.join(base_dir, args.second_file)
#first_file_path = base_dir / args.first_file
#   second_file_path = base_dir / args.second_file
#
#     print(json.dumps(args.first_filev, sort_keys=True, indent=4))
    dic_file1 = json.load(open(first_file_path))
    print(dic_file1)
    dic_file2 = json.load(open(second_file_path))
    print(dic_file2)
    
    print(diff_dicts(dic_file1, dic_file2))

    # Проверяем, существует ли файл
    if not os.path.exists(first_file_path):
        print(f"Файл не найден: {first_file_path}")
        return
    
    # Здесь будет логика вычисления отличий между файлами
    print("Difference Calculator is not implemented yet.")


if __name__ == "__main__":
    main()


