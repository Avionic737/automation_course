"""
Мы имеем файл с тестами, которые уже размечены маркерами для разных ситуаций запуска.

"""


import pytest


@pytest.mark.xfail(strict=True)
def test_succeed():
    assert True


@pytest.mark.xfail
def test_not_succeed():
    assert False


@pytest.mark.skip
def test_skipped():
    assert False

# Отметьте ниже только те тестовые методы, которые будут найдены и выполнены PyTest при запуске следующей команды:
# pytest -v -m "smoke and not beta_users" test_task_run_1.py
