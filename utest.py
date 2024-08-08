import pytest
import allure

@allure.feature('Feature1')
@allure.story('Story1')
@allure.severity(allure.severity_level.CRITICAL)
def test_example():
    assert 1 == 1

@allure.step('Step 1: Добавление двух чисел')
def add(a, b):
    return a + b

@allure.feature('Feature2')
@allure.story('Story2')
@allure.severity(allure.severity_level.NORMAL)
def test_add():
    result = add(1, 2)
    assert result == 3
