

API_HOSTS = {
    "test": "http://localhost:8888/apidemo/wp-json/wc/v3/",
    "dev": "",
    "prod": ""
}


WOO_API_HOSTS = {
    "test": "http://localhost:8888/apidemo/",
    "dev": "",
    "prod": ""
}



DB_HOST = {
    'machine1':{
        "test": {
            "host":"localhost",
            "database": "wp407",
            "table_prefix": "wpi_",
            "socket": None,
            "port": 8889
                 },
        "dev": {},
        "prod": {},
    },
    'docker':{
            "host":"host.docker.internal",
            "database": "wp407",
            "table_prefix": "wpi_",
            "socket": None,
            "port": 8889
    },
    'machine2':{}
}