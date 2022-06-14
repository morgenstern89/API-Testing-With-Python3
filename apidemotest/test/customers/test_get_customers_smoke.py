import pytest
import logging as logger
from apidemotest.src.utilities.requestsUtilities import RequestsUtilities

@pytest.mark.customers
@pytest.mark.tcid30
def test_get_all_customers():
    req_helper = RequestsUtilities()
    rs_api = req_helper.get('customers')

    assert rs_api, f"Response of list all customers is empty."


