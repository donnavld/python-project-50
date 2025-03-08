from gendiff.main import main
from io import StringIO
import sys
import pytest
import json
import yaml
from gendiff.script.compare_files import generate_diff
from gendiff.script.load_file import load_file
from gendiff.script.get_print import stylish, plain

def test_load_file(tmp_path):
    d = tmp_path / "sub"
    d.mkdir()
    p = d / "test.json"
    data = {"name": "Alice", "age": 25, "address": {"city": "NY", "street": "1-st street"}}
    p.write_text(json.dumps(data))
    expected = {"name": "Alice", "age": 25, "address":{"city":"NY", "street":"1-st street"}}
    assert load_file(__file__, "test.json") == expected

def test_load_file_invalid_format(tmp_path):
    d = tmp_path / "sub"
    d.mkdir()
    p = d / "test.txt"  # Неподдерживаемый формат .txt
    p.write_text("Some text content")

    with pytest.raises(ValueError, match="Unsupported file format: txt"):
        load_file(__file__, str(p))

def test_generate_diff():
    data1 = {"name": "Alice", "age": 25, "address":{"city":"NY", "street":"1-st street"}}
    data2 = {"name": "Alice", "age": 30, "email": "alice@example.com"}

    expected = {
        "name": "Alice",
        "age": {"-": 25, "+": 30},
        "address": {"-": {"city": "NY", "street": "1-st street"}},
        "email": {"+": "alice@example.com"}
    }

    assert generate_diff(data1, data2) == expected


def test_stylish():
    data = {
        "name": "Alice",
        "age": {"-": 25, "+": 30},
        "address": {"-": {"city": "NY", "street": "1-st street"}},
        "email": {"+": "alice@example.com"}
    }
    expected = """{
  name: Alice
  - age: 25
  + age: 30
  - address: {
      city: NY
      street: 1-st street
    }
  + email: alice@example.com
}"""
    assert stylish(data) == expected


def test_plain():
    data = {
        "name": "Alice",
        "age": {"-": 25, "+": 30},
        "address": {"-": {"city": "NY", "street": "1-st street"}},
        "email": {"+": "alice@example.com"},
        'setting5': {'+': {'key5': 'value5'}}
    }
    expected = """\
Property 'age' was updated. From 25 to 30
Property 'address' was removed
Property 'email' was added with value: 'alice@example.com'
Property 'setting5' was added with value: [complex value]
"""
    assert plain(data) == expected


def test_main_invalid_format(monkeypatch):
    test_args = ["hexlet-code", "tests/fixtures/file1.txt", "tests/fixtures/file2.txt"]
    monkeypatch.setattr(sys, "argv", test_args)

    with pytest.raises(ValueError, match="Unsupported file format: txt"):
        generate_diff()

def test_main(monkeypatch):
    test_args = ["python-project-50/modules", "tests/fixtures/file1.json", "tests/fixtures/file2.json"]
    monkeypatch.setattr(sys, "argv", test_args)
    captured_output = StringIO()
    monkeypatch.setattr(sys, "stdout", captured_output)
    generate_diff()
    output = captured_output.getvalue().strip()  # Получаем вывод и убираем лишние переносы строк
    expected = """{
  name: Alice
  - age: 25
  + age: 30
  - address: {
      city: NY
      street: 1-st street
    }
  + email: alice@example.com
}"""
    
    assert output == expected, f"Expected:\n{expected}\nGot:\n{output}"

# подмена даннных
#def test_main_with_monkeypatch(monkeypatch, capsys):
    # Подменяем глобальные данные, используемые в main()
#    monkeypatch.setattr("modules.script.main.some_global_data", {
        # новое значение для теста
#    })
    
#    main()
#    captured = capsys.readouterr().out.strip()
#    expected = "..."  # ожидаемый результат
#    assert captured == expected
