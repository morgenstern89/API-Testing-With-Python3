import pytest
from apidemotest.src.utilities.requestsUtilities import RequestsUtilities
from apidemotest.src.dao.products_dao import ProductsDAO
from apidemotest.src.helpers.products_helper import ProductsHelper

pytestmark = [pytest.mark.products, pytest.mark.smoke]

@pytest.mark.tcid24
def test_get_all_products():
        req_helper = RequestsUtilities()
        rs_api = req_helper.get(endpoint='products')

        # import pdb; pdb.set_trace()
        assert rs_api, f"Get all products endpoint returned nothing."



@pytest.mark.tcid25
def test_get_products_by_id():

        #get a product(test data) from db
        rand_product = ProductsDAO().get_random_product_from_db(1)
        rand_product_id=rand_product[0]['ID']
        db_name=rand_product[0]['post_title']

        #make the call
        product_helper=ProductsHelper()
        rs_api=product_helper.get_product_by_id(rand_product_id)
        api_name=rs_api['name']


        #verify the response
        assert db_name==api_name, f"Get product by id returned wrong product. ID: {rand_product_id}" \
                                  f"DB name: {db_name}, API name:{api_name}"
