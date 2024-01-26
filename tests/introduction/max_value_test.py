import pytest
import colorama
from colorama import Fore, Style
from Solutions.introduction.max_value import max_value

colorama.init(autoreset=True)

@pytest.mark.introduction
def test_00():
    try:
        result = max_value([4, 7, 2, 8, 10, 9])
        assert result == 10, f"Expected 10, got {result}"
        print(Fore.GREEN + f"\n\n\nTest passed for 00, expected 10, got {result}")
    except AssertionError as e:
        print(Fore.RED + "\nTest Failed: " + str(e))
