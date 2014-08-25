# -*- coding: utf-8 -*

INN_TEST_WEIGHTS_10 = (2, 4, 10, 3, 5, 9, 4, 6, 8, 0)
INN_TEST_WEIGHTS_12_0 = (7, 2, 4, 10, 3, 5, 9, 4, 6, 8, 0, 0)
INN_TEST_WEIGHTS_12_1 = (3, 7, 2, 4, 10, 3, 5, 9, 4, 6, 8, 0)


def test_inn_org(inn):
    """ returns True if inn of the organisation pass the check
    """
    if len(inn) != 10:
        return False

    res = 0
    for i, char in enumerate(inn):
        res += int(char) * INN_TEST_WEIGHTS_10[i]
    res = res % 11 % 10

    return res == int(inn[-1])


def test_inn_person(inn):
    """ returns True if inn of the person pass the check
    """
    if len(inn) != 12:
        return False

    res1 = 0
    for i, char in enumerate(inn):
        res1 += int(char) * INN_TEST_WEIGHTS_12_0[i]
    res1 = res1 % 11 % 10

    res2 = 0
    for i, char in enumerate(inn):
        res2 += int(char) * INN_TEST_WEIGHTS_12_1[i]
    res2 = res2 % 11 % 10

    return (res1 == int(inn[-2])) and (res2 == int(inn[-1]))


def test_inn(inn):
    """ returns True if inn pass the check
    """
    if len(inn) == 10:
        return test_inn_org(inn)
    elif len(inn) == 12:
        return test_inn_person(inn)

    return False

BANK_ACC_TEST_WEIGHTS = ((7, 1, 3) * 8)[:-1]


def test_bank_number(anumber):
    if not isinstance(anumber, str) and not anumber.isdigit():
        return False

    if len(anumber) != 23:
        return False

    res = 0
    for i, char in enumerate(anumber):
        res += int(char) * BANK_ACC_TEST_WEIGHTS[i]
    return (res % 10) == 0


def test_bank_corr_account_number(account, bik):
    return len(account) == 20 and len(bik) == 7 and \
        test_bank_number('0' + bik[4:6] + account)


def test_bank_account_number(account, bik):
    return len(account) == 20 and len(bik) == 7 and \
        test_bank_number(bik[-3:] + account)
