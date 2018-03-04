import date_simple as ds
import datetime as dt
import pytest

def test_get_date_object():
    assert ds.get_date_object() == dt.date.today()
    assert ds.get_date_object('2017-09-09') == dt.date(2017, 9, 9)
    with pytest.raises(ValueError):
        ds.get_date_object('09/09/2017')
    with pytest.raises(TypeError):
        ds.get_date_object(3)

def test_get_date_string():
    assert ds.get_date_string() == dt.date.today().strftime(format='%m/%d/%Y')
    assert ds.get_date_string(date=dt.date(2017, 9, 9)) == dt.date(2017, 9, 9).strftime(format='%m/%d/%Y')
    assert ds.get_date_string(format='MM/DD/YYYY') == dt.date.today().strftime(format='%m/%d/%Y')
    assert ds.get_date_string(format='DD-Mon-YY') == dt.date.today().strftime(format='%d-%b-%y')
    with pytest.raises(ValueError):
        ds.get_date_object('D/M/Y')
    with pytest.raises(TypeError):
        ds.get_date_string(3)


