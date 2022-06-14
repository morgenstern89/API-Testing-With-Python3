import pytest
from apidemotest.src.utilities.genericUtilities import generate_random_string
from apidemotest.src.helpers.products_helper import ProductsHelper
from apidemotest.src.dao.products_dao import ProductsDAO

pytestmark = [pytest.mark.products, pytest.mark.smoke]


@pytest.mark.tcid26
def test_create_simple_product():

    #generate some data
    payload=dict()
    payload['name']= generate_random_string(20)
    payload['type']= "simple"
    payload['regular_price']="10.99"

    #make the call
    product_rs=ProductsHelper().call_create_product(payload)

    #verify the response is not empty
    assert product_rs, f"Create product API response is empty. Payload: {payload}"
    assert product_rs['name']== payload['name'], f"Create product API call response has"\
    f"unexpected name. Expected {payload['name']}, Actual: {product_rs['name']}"

    #verify the product exists in db
    product_id=product_rs['id']
    db_product=ProductsDAO().get_product_by_id(product_id)

    assert payload['name']==db_product[0]['post_title'], f"Create product title in db does not match"\
    f"Title in API. DB: {db_product['post_title']}, API:{payload['name']}"

