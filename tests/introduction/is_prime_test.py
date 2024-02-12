import pytest
import colorama
from colorama import Fore, Style
from Solutions.introduction.is_prime import is_prime

colorama.init(autoreset=True)

@pytest.mark.introduction
@pytest.mark.is_prime
def test_00():
    try:
        result = is_prime(2)
        assert result == True, f"Expected True, got {result}"
        print(Fore.GREEN + f"\n\n\nTest passed for 00. Expected True, got {result}")
    except AssertionError as e:
        print(Fore.RED + "\nTest Failed: " + str(e))

@pytest.mark.introduction
@pytest.mark.is_prime
def test_01():
    try:
        result = is_prime(3)
        assert result == False, f"Expected False, got {result}"
        print(Fore.GREEN + f"\n\n\nTest passed for 01. Expected False, got {result}")
    except AssertionError as e:
        print(Fore.RED + "\nTest Failed: " + str(e))

@pytest.mark.introduction
@pytest.mark.is_prime
def test_02():
    try:
        result = is_prime(4)
        assert result == False, f"Expected True, got {result}"
        print(Fore.GREEN + f"\n\n\nTest passed for 02. Expected True, got {result}")
    except AssertionError as e:
        print(Fore.RED + "\nTest Failed: " + str(e))

@pytest.mark.introduction
@pytest.mark.is_prime
def test_03():
    try:
        result = is_prime(5)
        assert result == True, f"Expected True, got {result}"
        print(Fore.GREEN + f"\n\n\nTest passed for 03. Expected True, got {result}")
    except AssertionError as e:
        print(Fore.RED + "\nTest Failed: " + str(e))
    
@pytest.mark.introduction
@pytest.mark.is_prime
def test_04():
    try:
        result = is_prime(6)
        assert result == False, f"Expected False, got {result}"
        print(Fore.GREEN + f"\n\n\nTest passed for 04. Expected False, got {result}")
    except AssertionError as e:
        print(Fore.RED + "\nTest Failed: " + str(e))

@pytest.mark.introduction
@pytest.mark.is_prime
def test_05():
    try:
        result = is_prime(7)
        assert result == True, f"Expected True, got {result}"
        print(Fore.GREEN + f"\n\n\nTest passed for 05. Expected True, got {result}")
    except AssertionError as e:
        print(Fore.RED + "\nTest Failed: " + str(e))

@pytest.mark.introduction
@pytest.mark.is_prime
def test_06():
    try:
        result = is_prime(8)
        assert result == False, f"Expected False, got {result}"
        print(Fore.GREEN + f"\n\n\nTest passed for 06. Expected False, got {result}")
    except AssertionError as e:
        print(Fore.RED + "\nTest Failed: " + str(e))

@pytest.mark.introduction
@pytest.mark.is_prime
def test_07():
    try:
        result = is_prime(25)
        assert result == False, f"Expected False, got {result}"
        print(Fore.GREEN + f"\n\n\nTest passed for 07. Expected False, got {result}")
    except AssertionError as e:
        print(Fore.RED + "\nTest Failed: " + str(e))

@pytest.mark.introduction
@pytest.mark.is_prime
def test_08():
    try:
        result = is_prime(31)
        assert result == True, f"Expected True, got {result}"
        print(Fore.GREEN + f"\n\n\nTest passed for 08. Expected True, got {result}")
    except AssertionError as e:
        print(Fore.RED + "\nTest Failed: " + str(e))

@pytest.mark.introduction
@pytest.mark.is_prime
def test_09():
    try:
        result = is_prime(2017)
        assert result == True, f"Expected True, got {result}"
        print(Fore.GREEN + f"\n\n\nTest passed for 09. Expected True, got {result}")
    except AssertionError as e:
        print(Fore.RED + "\nTest Failed: " + str(e))

@pytest.mark.introduction
@pytest.mark.is_prime
def test_10():
    try:
        result = is_prime(2048)
        assert result == False, f"Expected False, got {result}"
        print(Fore.GREEN + f"\n\n\nTest passed for 10. Expected False, got {result}")
    except AssertionError as e:
        print(Fore.RED + "\nTest Failed: " + str(e))

@pytest.mark.introduction
@pytest.mark.is_prime
def test_11():
    try:
        result = is_prime(1)
        assert result == False, f"Expected False, got {result}"
        print(Fore.GREEN + f"\n\n\nTest passed for 11. Expected False, got {result}")
    except AssertionError as e:
        print(Fore.RED + "\nTest Failed: " + str(e))

@pytest.mark.introduction
@pytest.mark.is_prime
def test_12():
    try:
        result = is_prime(713)
        assert result == False, f"Expected False, got {result}"
        print(Fore.GREEN + f"\n\n\nTest passed for 12. Expected False, got {result}")
    except AssertionError as e:
        print(Fore.RED + "\nTest Failed: " + str(e))
