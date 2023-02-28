from utils import load_all_operation
from utils import get_n_operation
from utils import get_date
from utils import get_secret_card
from utils import get_secret_bill
from utils import is_bill


def test_load_all_operation():
    assert type(load_all_operation()) is list
    assert len(load_all_operation()) == 100


def test_get_n_operation():
    assert len(get_n_operation()) == 5
    assert len(get_n_operation(10)) == 10


def test_get_date():
    assert get_date('2019-08-26T10:50:58.294041') == '26.08.2019'


def test_get_secret_card():
    assert get_secret_card("MasterCard 7158300734726758") == "MasterCard 7158 30** **** 6758"
    assert get_secret_card("Visa Classic 6831982476737658") == "Visa Classic 6831 98** **** 7658"
    assert get_secret_card("Visa Platinum 8990922113665229") == "Visa Platinum 8990 92** **** 5229"
    assert get_secret_card("Maestro 3928549031574026") == "Maestro 3928 54** **** 4026"


def test_get_secret_bill():
    assert get_secret_bill("Счет 84163357546688983493") == "Счет **3493"


def test_is_bill():
    assert is_bill("Счет 84163357546688983493") is True
    assert is_bill("Visa Classic 6831982476737658") is False
