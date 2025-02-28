import json
import os    

def get_json_file(base_dir, file):

#    print (path_main)
    file_path = os.path.join(base_dir, file)
    dic_file = json.load(open(file_path))
#    print(dic_file)

# Проверяем, существует ли файл
    if not os.path.exists(file_path):
        print(f"Файл не найден: {file_path}")
        return
    
    return dic_file
