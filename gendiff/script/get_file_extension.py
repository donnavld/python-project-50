import os

def get_extension(file):
    _, ext = os.path.splitext(file)
    return ext.lstrip('.').lower() 
