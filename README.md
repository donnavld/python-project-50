### Hexlet tests and linter status:
[![Actions Status](https://github.com/donnavld/python-project-50/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/donnavld/python-project-50/actions)


# Diff Checker

## Установка
pip install my_diff_tool
## Использование 
gendiff file_c1.json file_c2.json

## Пример работы
```yaml
file1.yaml:
  name: Alice
  age: 25

file2.yaml:
  name: Alice
  age: 30
  email: alice@example.com

bash
$ generate_diff file1.yaml file2.yaml
{
    - age: 25
    + age: 30
    + email: alice@example.com
}
### **Что сделано**
✅ **Читаем файлы JSON/YAML**  
✅ **Находим различия и строим внутреннюю структуру diff**  
✅ **Выводим diff в удобном формате `stylish`**  
✅ 
✅ **Добавили документацию**

Теперь у нас есть **полноценный инструмент для поиска различий** между JSON/YAML-файлами с вложенными структурами!

