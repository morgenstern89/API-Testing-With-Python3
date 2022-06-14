import pytest
import random
from apidemotest.src.utilities.genericUtilities import generate_random_string
from apidemotest.src.helpers.products_helper import ProductsHelper
from apidemotest.src.dao.products_dao import ProductsDAO

pytestmark = [pytest.mark.products, pytest.mark.smoke]


@pytest.mark.tcid61
def test_update_regular_price():

    #verify updating the 'regular_price' field should automatically update the 'price' field.

    product_helper = ProductsHelper()
    product_dao = ProductsDAO()

    rand_products = product_dao.get_random_product_from_db(15)
    for product in rand_products:
        product_id=product['ID']
        product_data =product_helper.call_retrieve_product(product_id)
        if product_data['on_sale']:
            continue
        else:
            break
    else:
        test_product = random.choice(rand_products)
        product_id=test_product['ID']
        product_helper.call_update_product(product_id, {'sale_price': ''})


    #generate some data
    new_price=str(random.randint(10,100)) + '.' + str(random.randint(10,99))
    payload=dict()
    payload['regular_price']=new_price

    rs_update = product_helper.call_update_product(product_id, payload=payload)



    #verify the response is not empty
    assert rs_update['price']== new_price, f"Update product API call response. Updating the 'regular_price' did not"\
                                           f"update the 'price' field. Price field actual value: {rs_update['price']},"\
                                           f"expected value: {new_price}."
    assert rs_update['regular_price']== new_price, f"Update product API call response. Updating the 'regular_price' did not"\
                                                    f"update in the response. Actual response 'regular_price'={rs_update['price']},"\
                                                    f"but expected: {new_price}."


    rs_product=product_helper.call_retrieve_product(product_id)
    assert rs_product['price']==new_price, f"Update product API call response. Updating the 'regular price' did not"\
                                           f"update the 'price' field. Price field actual value: {rs_product['price']},"\
                                           f"expected value: {new_price}."
    assert rs_product['regular_price']==new_price, f"Update product API call response. Updating the 'regular_price' did not"\
                                                    f"update in the response. Actual response 'regular_price'={rs_product['price']},"\
                                                    f"but expected:{new_price}"




@pytest.mark.tcid63
@pytest.mark.tcid64
def test_update_sale_price():

    product_helper = ProductsHelper()

    #test case for on_sale=False
    regular_price = str(random.randint(10, 100)) + '.' + str(random.randint(10, 99))
    payload = dict()
    payload['name'] = generate_random_string(20)
    payload['type'] = "simple"
    payload['regular_price'] = regular_price
    product_info=product_helper.call_create_product(payload)
    product_id=product_info['id']
    assert not product_info['on_sale'], f"Newly crated product should not have 'on_sale=True'. Product id:{product_id}"
    assert not product_info['sale_price'], f"Newly crated product should not have value for 'sale_price' field."

    # Make 'update product' call with data for 'sale_price' that is greater than 0, on_sale=True
    sale_price= float(regular_price)*.75
    product_helper.call_update_product(product_id, {'sale_price':str(sale_price)})
    product_after_update=product_helper.call_retrieve_product(product_id)

    # Verify the 'on_sale' field of the product is updated to 'True'
    assert product_after_update['on_sale'], f"Update 'sale_price' of product, but the 'on_sale' is not 'True'."\
                                            f"Product id:{product_id}."

    # Make 'update product' call with empty string for 'sale_price' , 'on_sale' is False
    product_helper.call_update_product(product_id, {'sale_price': ''})
    product_after_update=product_helper.call_retrieve_product(product_id)

    # Verify the 'on_sale' field of the product is updated to 'False'
    assert not product_after_update['on_sale'], f"Update 'sale_price=""' of product, but the 'on_sale' is not 'False'." \
                                            f"Product id:{product_id}."



@pytest.mark.tcid65
def test_verify_and_update_sale_price():

    product_helper = ProductsHelper()
    product_dao = ProductsDAO()
    rand_products = product_dao.get_random_product_not_on_sale(1)
    product_id = rand_products[0]['ID']

    primary_info = product_helper.call_retrieve_product(product_id)
    assert not primary_info['on_sale'], f"Get data with 'on_sale=False' but got 'on_sale=True'. Unable to use this for test." \

    sale_price = float(primary_info['regular_price']) * .75

    payload = dict()
    payload['sale_price'] = str(sale_price)
    product_helper.call_update_product(product_id, payload=payload)

    after_info = product_helper.call_retrieve_product(product_id)
    assert after_info['sale_price'] == str(sale_price), f"Update 'sale_price' of the product but it is not updated." \
                                                        f"Product id:{product_id}, Expected sale price:{sale_price},"\
                                                        f"Actual sale price:{after_info['sale_price']}"
