from modules.script.main import main

def fake_get_repos(self):
        return [
            type('Repo', (), {'name': 'repo1', 'fork': True})(),
            type('Repo', (), {'name': 'repo2', 'fork': False})(),
            type('Repo', (), {'name': 'repo3', 'fork': True})()
        ]

def test_main(capsys):
    main()
    # Захватываем вывод
    captured = capsys.readouterr().out.strip()    
    expected = (
        "host: hexlet.io\n"
        "- timeout: 50\n"
        "+ timeout: 20\n"
        "- follow: False\n"
        "- proxy: 123.234.53.22\n"
        "+ verbose: True"
    )
    
    assert captured == expected

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
