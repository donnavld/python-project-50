import os  
from .get_json import get_json_file
from .get_yaml import get_yaml_file
from .get_file_extension import get_extension

def load_file(file, filepath):
    ext = get_extension(filepath).lower()
    base_dir = os.path.join(os.path.dirname(file), "", "files")
    loaders = {"json": get_json_file, "yml": get_yaml_file, "yaml": get_yaml_file}
    if ext in loaders:
        return loaders[ext](base_dir, filepath)
    raise ValueError(f"Unsupported file format: {ext}")
