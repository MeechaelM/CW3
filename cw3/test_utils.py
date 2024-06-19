from cw3.utils import sorted_operations_status, sorted_operations_date, message, mask_card_number, mask_account_number, mask_in_message, format_date

import pytest

def test_sorted_operations_status():
  assert (len(sorted_operations_status([{"state": "EXECUTED"}, {"state": "CANCELED"}])) == 1)

def test_sorted_operations_date():
  assert sorted_operations_date([{"date": "2019-07-12T20:41:47.882230"}, {"date": "2018-08-19T04:27:37.904916"}, {"date": "2018-12-28T23:10:35.459698"}])

def test_mask_card_number():
  assert mask_card_number('4111111111111111') == '4111 11** **** 1111'
  with pytest.raises(ValueError):
    assert mask_card_number('111111111111111')
  with pytest.raises(ValueError):
    assert mask_card_number('')

def test_mask_account_number():
  assert mask_account_number('17066032701791012883') == '**2883'
  with pytest.raises(ValueError):
    assert mask_account_number('70660')
  with pytest.raises(ValueError):
    assert mask_account_number('')

def test_mask_in_message():
  assert mask_in_message('Счет 17066032701791012883') == 'Счет **2883'
  assert mask_in_message('Visa Platinum 7825450883088021') == 'Visa Platinum 7825 45** **** 8021'
  assert mask_in_message('Visa Classic 8906171742833215') == 'Visa Classic 8906 17** **** 3215'
  assert mask_in_message('МИР 8021883699486544') == 'МИР 8021 88** **** 6544'
  assert mask_in_message('Visa Gold 8702717057933248') == 'Visa Gold 8702 71** **** 3248'
  assert mask_in_message('Maestro 6890749237669619') == 'Maestro 6890 74** **** 9619'
  assert mask_in_message('MasterCard 9454780748494532') == 'MasterCard 9454 78** **** 4532'

def test_message():
  assert message({
    "date": "2022-02-22T22:22:22.222222",
    "description": "Перевод организации",
    "from": "Счет 12221222122212221222",
    "operationAmount": {
      "amount": "222222.22",
      "currency": {
        "name": "руб."}},
    "to": "Счет 32223222322232223223"
    }) == '2022-02-22 Перевод организации\nСчет **1222 -> Счет **3223\n222222.22 руб.'

def test_format_date():
  assert format_date('2022-02-22T22:22:22.222222') == '22.02.2022'
  assert format_date('2000-01-11T11:22:33.123456') == '11.01.2000'
  assert format_date('2019-05-06T00:20:03.056245') == '06.05.2019'