### Hexlet tests and linter status:
[![Actions Status](https://github.com/donnavld/python-project-50/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/donnavld/python-project-50/actions)


# Diff Checker

## Установка
pip install my_diff_tool
## Использование default format = stylish
gendiff file_c1.json file_c2.json
gendiff --format plain file_c1.yml file_c2.yml

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

```json
file_c1.json:
  name: Alice
  age: 25

file_c2.json:
  "name": "Alice"
  "age": 30
  "email": "alice@example.com"
  "setting5": {
    "key5": "value5"
  }
bash
$ gendiff --format plain file_c1.json file_c2.json
{
  Property 'age' was updated. From 25 to 30
  Property 'address' was removed
  Property 'email' was added with value: 'alice@example.com'
  Property 'setting5' was added with value: [complex value]
}

### **Что сделано**
✅ **Читаем файлы JSON/YAML**  
✅ **Находим различия и строим внутреннюю структуру diff**  
✅ **Выводим diff в удобном формате `stylish`**  
✅ 
✅ **Добавили документацию**

Теперь у нас есть **полноценный инструмент для поиска различий** между JSON/YAML-файлами с вложенными структурами!

