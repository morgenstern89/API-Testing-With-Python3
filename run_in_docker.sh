source ./env_docker.sh
#DATE_WITH_TIME= `date "+%Y%m%d_%H%M%S"`

set -x
docker run --rm -it  \
-v $(pwd)/apidemotest:/automation/apidemotest \
-e wc_key=${WC_KEY} \
-e wc_secret=${WC_SECRET} \
-e wp_host=${WP_HOST} \
-e machine=${MACHINE} \
-e db_user=${DB_USER} \
-e db_password=${DB_PASSWORD} \
apidemo_test \
pytest -c /automation/apidemotest/pytest.ini \
--color=yes \
--html /automation/apidemotest/reports/result.html \
-m "$1" /automation/apidemotest

