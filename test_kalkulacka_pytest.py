# test_kalkulacka_pytest.py - Projekt 11, Etapa 3: testy v style PYTEST.
# Spustenie:  python -m pytest test_kalkulacka_pytest.py -v
# pytest sam najde funkcie zacinajuce na "test_" a spusti ich. Staci pouzit "assert".

import kalkulacka as k


def test_scitaj():
    assert k.scitaj([2, 7]) == 9


def test_odcitaj():
    assert k.odcitaj([8, 6]) == 2


def test_nasob():
    assert k.nasob([5, 8]) == 40


def test_vydel():
    assert k.vydel([8, 2]) == 4


def test_delenie_nulou_vrati_none():
    assert k.vydel([8, 0]) is None
