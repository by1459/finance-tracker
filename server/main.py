import os

import plaid
from fastapi import FastAPI
from plaid.api import plaid_api
from plaid.model.country_code import CountryCode
from plaid.model.item_public_token_exchange_request import (
    ItemPublicTokenExchangeRequest,
)
from plaid.model.link_token_create_request import LinkTokenCreateRequest
from plaid.model.link_token_create_request_user import LinkTokenCreateRequestUser
from plaid.model.products import Products
from pydantic import BaseModel, ConfigDict, alias_generators
from pydantic.alias_generators import to_camel

app = FastAPI()

PLAID_CLIENT_ID = os.getenv("PLAID_CLIENT_ID")
PLAID_SECRET = os.getenv("PLAID_SECRET")
PLAID_ENV = os.getenv("PLAID_ENV")

USER = "user"

host = plaid.Environment.Sandbox
if PLAID_ENV == "sandbox":
    host = plaid.Environment.Sandbox
if PLAID_ENV == "production":
    host = plaid.Environment.Production

configuration = plaid.Configuration(
    host=host,
    api_key={
        "clientId": PLAID_CLIENT_ID,
        "secret": PLAID_SECRET,
    },
)


api_client = plaid.ApiClient(configuration)
plaid_client = plaid_api.PlaidApi(api_client)


class CamelModel(BaseModel):
    model_config = ConfigDict(alias_generator=to_camel, populate_by_name=True)


class Transaction(CamelModel):
    transaction_id: str
    account_id: str
    amount: int
    counterparty: str
    date: int
    category: str


class LinkTokenResponse(CamelModel):
    link_token: str


@app.post("/api/create_link_token")
def create_link_token() -> LinkTokenResponse:
    request = LinkTokenCreateRequest(
        products=[Products("transactions")],
        client_name="Brian's very cool test app",
        country_codes=[CountryCode("US")],
        language="en",
        user=LinkTokenCreateRequestUser(client_user_id=USER),
    )
    response = plaid_client.link_token_create(request)
    return response.to_dict()


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
