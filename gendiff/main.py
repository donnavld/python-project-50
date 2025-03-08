import argparse
from .script.get_file_extension import get_extension 
from .script.compare_files import diff_dict, generate_diff
from .script.stylish import stylish
from .script.load_file import load_file


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


