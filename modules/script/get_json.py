import json
import os    

def get_json_file(path_main, file):

    base_dir = os.path.join(os.path.dirname(path_main), "", "files")
#    print (path_main)
    file_path = os.path.join(base_dir, file)
    dic_file = json.load(open(file_path))
#    print(dic_file)

# Проверяем, существует ли файл
    if not os.path.exists(file_path):
        print(f"Файл не найден: {file_path}")
        return
    
    return dic_file
