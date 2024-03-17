import pytest
from datetime import date
from model import Batches, OrderRealm


def test_order_realm_on_one_year():
    batch = Batches(nr=["realm1", "realm2", "realm3"], cr=3)
    order = OrderRealm(
        name_realm="realm4",
        date_start=date.today(),
        date_end=date.today().replace(year=date.today().year + 1),
    )

    batch.order_realm(order)

    assert batch.count_realm == 4


def test_order_realm_on_one_month():
    batch = Batches(nr=["realm1", "realm2", "realm3"], cr=3)
    order = OrderRealm(
        name_realm="realm4",
        date_start=date.today(),
        date_end=date.today().replace(month=date.today().month + 1),
    )

    batch.order_realm(order)

    assert batch.count_realm == 4


def test_order_realm_on_one_day():
    batch = Batches(nr=["realm1", "realm2", "realm3"], cr=3)
    order = OrderRealm(
        name_realm="realm4",
        date_start=date.today(),
        date_end=date.today().replace(day=date.today().day + 1),
    )

    batch.order_realm(order)

    assert batch.count_realm == 4


def test_order_realm_failed_date():
    batch = Batches(nr=["realm1", "realm2", "realm3"], cr=3)
    order = OrderRealm(
        name_realm="realm4",
        date_start=date.today(),
        date_end=date.today().replace(year=date.today().year - 1),
    )

    with pytest.raises(ValueError):
        batch.order_realm(order)


def test_order_realm_failed_argument_all():
    with pytest.raises(
        TypeError,
        match=r"argument: 'name_realm'",
    ):
        OrderRealm(
            date_start=date.today(),
            date_end=date.today().replace(year=date.today().year - 1),
        )
    with pytest.raises(
        TypeError,
        match=r"argument: 'date_start'",
    ):
        OrderRealm(
            name_realm="realm4",
            date_end=date.today().replace(year=date.today().year - 1),
        )
    with pytest.raises(
        TypeError,
        match=r"argument: 'date_end'",
    ):
        OrderRealm(
            name_realm="realm4",
            date_start=date.today(),
        )
    with pytest.raises(TypeError):
        OrderRealm()


def test_order_realm_values_other_type():
    with pytest.raises(TypeError):
        OrderRealm(
            name_realm=12345,
            date_start=date.today(),
            date_end=date.today().replace(month=date.today().month + 1),
        )
    with pytest.raises(TypeError):
        OrderRealm(
            name_realm=date.today(),
            date_start=date.today(),
            date_end=date.today().replace(month=date.today().month + 1),
        )
    with pytest.raises(TypeError):
        OrderRealm(
            name_realm="realm4",
            date_start=555,
            date_end=date.today().replace(month=date.today().month + 1),
        )
    with pytest.raises(TypeError):
        OrderRealm(
            name_realm="realm4",
            date_start="2024-03-17",
            date_end=date.today().replace(month=date.today().month + 1),
        )
    with pytest.raises(TypeError):
        OrderRealm(name_realm="realm4", date_start=date.today(),
                   date_end="2024-03-17")

    with pytest.raises(TypeError):
        OrderRealm(name_realm="realm4", date_start=date.today(), date_end=5555)
