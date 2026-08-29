import os

import plaid
from fastapi import FastAPI
from plaid.api import plaid_api
from pydantic import BaseModel, ConfigDict, alias_generators
from pydantic.alias_generators import to_camel

app = FastAPI()


class CamelModel(BaseModel):
    model_config = ConfigDict(alias_generator=to_camel, populate_by_name=True)


class Transaction(CamelModel):
    transaction_id: str
    account_id: str
    amount: int
    counterparty: str
    date: int
    category: str


@app.get("/api/get_transaction")
def get_transaction() -> Transaction:
    return Transaction(
        transaction_id="1",
        account_id="2",
        amount=20,
        counterparty="hello",
        date=2,
        category="greetings",
    )


def main():
    print("Hello from server!")


if __name__ == "__main__":
    main()
