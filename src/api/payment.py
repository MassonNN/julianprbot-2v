import decimal
from dataclasses import dataclass


@dataclass
class PaymentCase:
    user_id: int
    value: decimal.Decimal


@dataclass
class PayoutCase:
    user_id: int
    value: decimal.Decimal


def get_payment_url(payment_case: PaymentCase) -> str:
    return 'someurl.com/' + str(payment_case.value)
