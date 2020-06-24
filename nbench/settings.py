MONGO_HOST = 'localhost'
MONGO_PORT = 27017

MONGO_AUTH_SOURCE = '<dbname>'

MONGO_DBNAME = 'nbench'
RESOURCE_METHODS = ['GET', 'POST', 'DELETE']
ITEM_METHODS = ['GET', 'PATCH', 'PUT', 'DELETE']
URL_PREFIX = "api"


benchmark_schema = {
    'BenchmarkName': {
        'type': 'string',
        'minlength': 3,
        'maxlength': 50,
        'required': True,
    },
    'Workloads': {
        'type': 'list',
        'required': True,
    },
    'Description': {
        'type': 'string',
        'required': False,
    },
    'DatastoreName': {
        'type': 'string',
        'required': True,
    }
}
vCenter_schema = {
    'username': {
        'type': 'string',
        'minlength': 3,
        'maxlength': 50,
        'required': True,
    },
    'password': {
        'type': 'string',
        'minlength': 3,
        'maxlength': 50,
        'required': True,
    },
    'address': {
        'type': 'string',
        'minlength': 3,
        'maxlength': 50,
        'required': True,
    }
}

workload_schema = {
    'WorkloadName': {
        'type': 'string',
        'minlength': 3,
        'maxlength': 50,
        'required': True,
    },
    'readWrite': {
        'type': 'string',
        # TODO: Add the rest of the supported types
        #  https://fio.readthedocs.io/en/latest/fio_doc.html
        'allowed': ["read", "write", "randread", "randwrite", 'randrw'],
        'required': True,
    },
    'ioEngine': {
        'type': 'string',
        # TODO: Add the rest of the supported types from section 1.12.10. I/O engine at
        #  https://fio.readthedocs.io/en/latest/fio_doc.html
        'allowed': ["sync", "psync", "vsync", "pvsync", "pvsync2", "io_uring", "libaio", "posixaio"]
    },
    'blockSize': {
        'type': 'string',
        'minlength': 1,
        'maxlength': 50,
        'required': True
    },
    'fileSize': {
        'type': 'string',
        'minlength': 1,
        'maxlength': 50,
        'required': True
    },
    'runTime': {
        'type': 'number',
        'required': True
    }
}


# Define each workload configuration
workload = {
    'item_title': 'workload',
    'additional_lookup': {
        'url': 'regex("[\w]+")',
        'field': '_id'
    },
    'resource_methods': ['GET', 'POST'],
    'schema': workload_schema
}

# Group different benchmarks into a test
benchmark = {
    'item_title': 'benchmark',
    'resource_methods': ['GET', 'POST'],
    'schema': benchmark_schema
}

vCenter = {
    'item_title': 'vCenter',
    'resource_methods': ['GET', 'POST'],
    'schema': vCenter_schema
}

DOMAIN = {
    'workload': workload,
    'benchmark': benchmark,
    'settings/vCenter': vCenter,

}
