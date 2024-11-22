from b import solve

import io


def test_b_solve_1(capsys, monkeypatch):
    acutual = """\

"""
    monkeypatch.setattr('sys.stdin', io.StringIO(acutual))
    solve()
    expected = """\

"""
    assert capsys.readouterr().out == expected


def test_b_solve_2(capsys, monkeypatch):
    acutual = """\

"""
    monkeypatch.setattr('sys.stdin', io.StringIO(acutual))
    solve()
    expected = """\

"""
    assert capsys.readouterr().out == expected


def test_b_solve_3(capsys, monkeypatch):
    acutual = """\

"""
    monkeypatch.setattr('sys.stdin', io.StringIO(acutual))
    solve()
    expected = """\

"""
    assert capsys.readouterr().out == expected


def test_b_solve_4(capsys, monkeypatch):
    acutal = """\

"""
    monkeypatch.setattr('sys.stdin', io.StringIO(acutal))
    solve()
    expected = """\

"""
    assert capsys.readouterr().out == expected
