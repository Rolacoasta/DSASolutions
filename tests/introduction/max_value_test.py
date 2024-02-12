import pytest
import colorama
from colorama import Fore, Style
from Solutions.introduction.max_value import max_value

colorama.init(autoreset=True)

@pytest.mark.introduction
@pytest.mark.max_value
def test_00():
    try:
        result = max_value([4, 7, 2, 8, 10, 9])
        assert result == 10, f"Expected 10, got {result}"
        print(Fore.GREEN + f"\n\n\nTest passed for 00. Expected 10, got {result}")
    except AssertionError as e:
        print(Fore.RED + "\nTest Failed: " + str(e))

@pytest.mark.introduction
@pytest.mark.max_value
def test_01():
    try:
        result = max_value([10, 5, 40, 40.3])
        assert result == 40.3, f"Expected 40.3, got {result}"
        print(Fore.GREEN + f"\n\n\nTest passed for 01. Expected 40.3, got {result}")
    except AssertionError as e:
        print(Fore.RED + "\nTest Failed: " + str(e))

@pytest.mark.introduction
@pytest.mark.max_value
def test_02():
    try:
        result = max_value([-5, -2, -1, -11])
        assert result == -1, f"Expected, -1, got {result}"
        print(Fore.GREEN + f"\n\n\nTest passed for 02. Expected -1, got {result}")
    except AssertionError as e:
        print(Fore.RED + "\nTest Failed: " + str(e))

@pytest.mark.introduction
@pytest.mark.max_value
def test_03():
    try:
        result = max_value([42])
        assert result == 42, f"Expected, 42, got {result}"
        print(Fore.GREEN + f"\n\n\nTest passed for 03. Expected 42, got {result}")
    except AssertionError as e:
        print(Fore.RED + "\nTest Failed: " + str(e))

@pytest.mark.introduction
@pytest.mark.max_value
def test_04():
    try:
        result = max_value([1000, 8])
        assert result == 1000, f"Expected, 1000, got {result}"
        print(Fore.GREEN + f"\n\n\nTest passed for 04. Expected 1000, got {result}")
    except AssertionError as e:
        print(Fore.RED + "\nTest Failed: " + str(e))

@pytest.mark.introduction
@pytest.mark.max_value
def test_05():
    try:
        result = max_value([1000, 8, 9000])
        assert result == 9000, f"Expected, 9000, got {result}"
        print(Fore.GREEN + f"\n\n\nTest passed for 05. Expected 9000, got {result}")
    except AssertionError as e:
        print(Fore.RED + "\nTest Failed: " + str(e))

@pytest.mark.introduction
@pytest.mark.max_value
def test_06():
    try:
        result = max_value([2, 5, 1, 1, 4])
        assert result == 5, f"Expected, 5, got {result}"
        print(Fore.GREEN + f"\n\n\nTest passed for 06. Expected 5, got {result}")
    except AssertionError as e:
        print(Fore.RED + "\nTest Failed: " + str(e))