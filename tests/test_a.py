from a import solve

import io


def test_a_solve_1(capsys, monkeypatch):
    actual = """\

"""
    monkeypatch.setattr('sys.stdin', io.StringIO(actual))
    solve()
    expected = """\

"""
    assert capsys.readouterr().out == expected


def test_a_solve_2(capsys, monkeypatch):
    actual = """\

"""
    monkeypatch.setattr('sys.stdin', io.StringIO(actual))
    solve()
    expected = """\

"""
    assert capsys.readouterr().out == expected


def test_a_solve_3(capsys, monkeypatch):
    actual = """\

"""
    monkeypatch.setattr('sys.stdin', io.StringIO(actual))
    solve()
    expected = """\

"""
    assert capsys.readouterr().out == expected


def test_a_solve_4(capsys, monkeypatch):
    acutal = """\

"""
    monkeypatch.setattr('sys.stdin', io.StringIO(acutal))
    solve()
    expected = """\

"""
    assert capsys.readouterr().out == expected
