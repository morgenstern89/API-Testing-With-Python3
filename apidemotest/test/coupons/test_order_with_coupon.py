import pytest
import random
import logging as logger
from apidemotest.src.utilities.genericUtilities import generate_random_coupon_code, generate_random_string
from apidemotest.src.helpers.coupons_helper import CouponsHelper
from apidemotest.src.utilities.wooAPIUtility import WooAPIUtility

pytestmark = [pytest.mark.regression, pytest.mark.coupons]


@pytest.fixture(scope='module')
# Create/ find a coupon that is 50% off
def create_coupon():

    info={}
    info['coupon_helper']=CouponsHelper()

    return(info)

@pytest.mark.parametrize("discount_type",
                         [pytest.param(None, marks=[pytest.mark.tcid36, pytest.mark.smoke]),
                          pytest.param('percent', marks=[pytest.mark.tcid37, pytest.mark.smoke]),
                          pytest.param('fixed_product', marks=pytest.mark.tcid38),
                          pytest.param('fixed_cart', marks=pytest.mark.tcid39)
                          ])
def test_order_with_fifty_percent_coupon(create_coupon, discount_type):

    logger.info("Testing create coupon API for 50% discount")

    expected_discount_type=discount_type if discount_type else 'fixed_cart'
    percentage_off = str(random.randint(50,90)) + ".00"
    coupon_code = generate_random_coupon_code(suffix="tcid37", length=5)
    coupon_helper = create_coupon['coupon_helper']

    payload = dict()
    payload['code'] = coupon_code
    payload['amount'] = percentage_off

    if discount_type:
        payload['discount_type']=discount_type
    rs_coupon = coupon_helper.call_create_coupon(payload=payload)
    coupon_id=rs_coupon['id']

    rs_coupon_2=coupon_helper.call_retrieve_coupon(coupon_id)

    assert rs_coupon_2['amount'] == percentage_off, f"Create coupon with 50% discount responded {rs_coupon_2['amount']} for amount."\
                                                  f"Expected: {percentage_off}, Actual: {rs_coupon_2['amount']}."

    assert rs_coupon_2['code'] == coupon_code.lower(), f"Create coupon response has wrong 'code'."\
                                                     f"Expected:{coupon_code.lower()}, Actual: {rs_coupon_2['code']}."
    assert rs_coupon_2['discount_type']==expected_discount_type, f"Create coupon responded with wrong 'discount_type'."\
                                                                f"Expected:{expected_discount_type}, Actual:{rs_coupon_2['discount_type']}"



@pytest.mark.tcid40
def test_create_coupon_with_valid_discount_type():

    logger.info("Testing create coupon API with invalid 'discount_type'.")

    payload = dict()
    payload['code'] = generate_random_coupon_code(suffix="tcid40",length=5)
    payload['amount'] = str(random.randint(50,90)) + ".00"
    payload['discount_type'] = generate_random_string()
    rs_coupon=WooAPIUtility().post('coupons', params=payload, expected_status_code=400)

    assert rs_coupon['code'] == 'rest_invalid_param', f"Create coupon with invalid 'discount_type'" \
                                                       f"returned 'code={rs_coupon['code']}', Expected code='rest_invalid_param'."
    assert rs_coupon['message'] == 'Invalid parameter(s): discount_type', f"Create coupon with invalid 'discount_type'" \
                                                           f"Expected:'Invalid parameter(s):discount_type', Actual:'message={rs_coupon['message']}'."