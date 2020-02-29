import logging
# import logstash
import sys
# import logstash_async
from logstash_async.handler import AsynchronousLogstashHandler

logger = logging.getLogger('python-logstash-logger')
logger.setLevel(logging.INFO)
logger.addHandler(AsynchronousLogstashHandler(
    '0.0.0.0', 8080, database_path=None))


# Logging
extra = {
    'test_string': 'python version: ' + repr(sys.version_info),
    'test_boolean': True,
    'test_dict': {'a': 1, 'b': 'f'},
    'test_float': 1.23,
    'test_integer': 123,
    'test_list': [1, 2, '3'],
}
logger.info('python-logstash: test extra fields', extra=extra)
