import importlib
rem_mod = importlib.import_module("Code.16_remove_duplicates")

def test_remove_duplicates():
    assert rem_mod.remove_duplicates([1, 2, 2, 3, 1]) == [1, 2, 3]