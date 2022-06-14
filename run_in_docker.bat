source ./env_docker.bat

docker run --rm ^
-it -v %CD%\apidemotest:/automation/apidemotest/ ^
-e WC_KEY=%WC_KEY% ^
-e WC_SECRET=%WC_SECRET% ^
-e WP_HOST=%WP_HOST% ^
-e MACHINE=%MACHINE% ^
-e DB_USER=%DB_USER% ^
-e DB_PASSWORD=%DB_PASSWORD% ^
apidemo_test ^
pytest -c /automation/apidemotest/pytest.ini ^

--html /automation/apidemotest/reports/result.html ^
-m "$1" /automation/apidemotest


