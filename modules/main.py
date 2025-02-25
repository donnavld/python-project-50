import argparse
from .script.get_file_extension import get_extension 
from .script.compare_files import diff_dicts
from .script.get_json import get_json_file
from .script.get_yaml import get_yaml_file


def main():
#    print("Hello from python-project-50!")
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
        choices=['yaml', 'json'],
        default='json'
        ) 
    args = parser.parse_args()

    extension_f1 = get_extension(args.first_file).lower() 
    extension_f2 = get_extension(args.second_file).lower() 
#    print (extension_f1)
    if extension_f1 == "json":
#        print("Файл в формате JSON")
        dic_file1 = get_json_file(__file__, args.first_file)
#        dic_file2 = get_json_file(__file__, args.second_file)
    elif extension_f1 == "yml" or extension_f1 == "yaml":
#        print("Файл в формате YAML")
        dic_file1 = get_yaml_file(__file__, args.first_file)
#        print(dic_file1)
    
    if extension_f2 == "json":
#        print("Файл в формате JSON")
        dic_file2 = get_json_file(__file__, args.second_file)
    elif extension_f2 == "yml" or extension_f2 == "yaml":
#        print("Файл в формате YAML")
        dic_file2 = get_yaml_file(__file__, args.second_file)
    
#     print(json.dumps(args.first_filev, sort_keys=True, indent=4))
    print(diff_dicts(dic_file1, dic_file2))    
    


if __name__ == "__main__":
    main()


