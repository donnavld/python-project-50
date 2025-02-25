import yaml
import os   

def get_yaml_file(path_main, file):

    base_dir = os.path.join(os.path.dirname(path_main), "", "files")
#    print (path_main)
    file_path = os.path.join(base_dir, file)
#    print (file_path)
    with open(file_path, "r", encoding="utf-8") as f:
        dic_file = yaml.safe_load(f)
#    print (dic_file)


# Проверяем, существует ли файл
    if not os.path.exists(file_path):
        print(f"Файл не найден: {file_path}")
        return
    
    return dic_file
