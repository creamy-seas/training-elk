import requests
import logging
from logstash_async.handler import AsynchronousLogstashHandler
from logstash_async.formatter import LogstashFormatter

# 1 - get the logger for logstash #############################################
logger = logging.getLogger('python-logstash-logger')
logger.setLevel(logging.INFO)

# 2 - create logstash handler #################################################
# set the host, port, and any ssl values
lg_handler = AsynchronousLogstashHandler(
    'elkdreams-ai.com', 8080, database_path=None)

# 3 - define formatting options ###############################################
lg_formatter = LogstashFormatter(
    message_type='execution_analysis',
    extra_prefix='custom_data')

# 4 - apply formatting and add the handler ####################################
lg_handler.setFormatter(lg_formatter)
logger.addHandler(lg_handler)


###############################################################################
#                                Test requests                             #
###############################################################################
extra = {
    'bank': 'ICBC',
    'bank_account': 'bb56893',
    'function': 'Yelp',
    'function_ancestors': ['test1', 'test2', 'test3'],
    'success': True,
    'clientip': requests.get('http://ip.42.pl/raw').text
}
#logger.info("Report on execution of a bank function", extra=extra)
#print("sensinge")

    
def run_logger(func):
    def wrapper(*args, **kwargs):
        print('done')
        logger.info("Report on execution of a bank function", extra=extra)
        return_val = func()
        return return_val
    return wrapper
