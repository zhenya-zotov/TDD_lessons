from dataclasses import dataclass
from datetime import date
from typing import List


@dataclass
class OrderRealm:
    name_realm: str
    date_start: date
    date_end: date

    def __post_init__(self):
        if not isinstance(self.name_realm, str):
            raise TypeError("`name_realm` must be a string")
        if not isinstance(self.date_start, date):
            raise TypeError("`date_start` must be an date")
        if not isinstance(self.date_end, date):
            raise TypeError("`date_end` must be an date")


class Batches:
    def __init__(self, nr: List[str], cr: int):
        self.name_realms = nr
        self.count_realm = cr

    def order_realm(
        self,
        list_realm: OrderRealm,
    ):
        self.date_start = list_realm.date_start
        self.date_end = list_realm.date_end

        if self.date_start > self.date_end:
            raise ValueError(
                "`date_start` must be greater than or equal to `date_end`."
            )

        self.name_realms.append(list_realm.name_realm)
        self.count_realm += 1
