import pytest
from verifica_premio import parse_user_numbers, check_number_in_list, main


def test_parse_user_numbers_valid():
    assert parse_user_numbers("1 2 3") == [1, 2, 3]


def test_parse_user_numbers_invalid():
    with pytest.raises(ValueError):
        parse_user_numbers("a b c")


def test_parse_user_numbers_empty():
    with pytest.raises(ValueError):
        parse_user_numbers("  ")


def test_check_number_in_list_true():
    assert check_number_in_list([1, 2, 3], 2) is True


def test_check_number_in_list_false():
    assert check_number_in_list([1, 2, 3], 5) is False


def test_main_winner(monkeypatch, capsys):
    inputs = iter(["1 2 3", "2"])
    monkeypatch.setattr('builtins.input', lambda prompt='': next(inputs))
    main()
    captured = capsys.readouterr()
    assert "Parabéns! Você ganhou!" in captured.out


def test_main_invalid_then_win(monkeypatch, capsys):
    inputs = iter(["4 5 6", "x", "5"])
    monkeypatch.setattr('builtins.input', lambda prompt='': next(inputs))
    main()
    captured = capsys.readouterr()
    assert "Entrada inválida. Por favor, digite um número inteiro." in captured.out
    assert "Parabéns! Você ganhou!" in captured.out
