MONGO_HOST = 'localhost'
MONGO_PORT = 27017

MONGO_AUTH_SOURCE = '<dbname>'

MONGO_DBNAME = 'nbench'
RESOURCE_METHODS = ['GET', 'POST', 'DELETE']
ITEM_METHODS = ['GET', 'PATCH', 'PUT', 'DELETE']
URL_PREFIX = "api"


benchmark_schema = {
    'name': {
        'type': 'string',
        'minlength': 3,
        'maxlength': 50,
        'required': True,
    },
    'workload': {
        'type': 'list',
        'required': True,
    }
}

workload_schema = {
    'name': {
        'type': 'string',
        'minlength': 3,
        'maxlength': 50,
        'required': True,
    },
    'rw': {
        'type': 'string',
        # TODO: Add the rest of the supported types
        #  https://fio.readthedocs.io/en/latest/fio_doc.html
        'allowed': ["read", "write", "randread", "randwrite", 'randrw'],
        'required': True,
    },
    'ioengine': {
        'type': 'string',
        # TODO: Add the rest of the supported types from section 1.12.10. I/O engine at
        #  https://fio.readthedocs.io/en/latest/fio_doc.html
        'allowed': ["sync", "psync", "vsync", "pvsync", "pvsync2", "io_uring", "libaio", "posixaio"]
    },
    'blocksize': {
        'type': 'string',
        'minlength': 1,
        'maxlength': 50,
        'required': True
    },
    'size': {
        'type': 'string',
        'minlength': 1,
        'maxlength': 50,
        'required': True
    },
    'runtime': {
        'type': 'number',
        'required': True
    }
}


# Define each workload configuration
workload = {
    'item_title': 'workload',
    'resource_methods': ['GET', 'POST', 'DELETE'],
    'schema': workload_schema
}

# Group different benchmarks into a test
benchmark = {
    'item_title': 'test',
    'resource_methods': ['GET', 'POST', 'DELETE'],
    'schema': benchmark_schema
}

DOMAIN = {
    'workload': workload,
    'test_group': benchmark

}
