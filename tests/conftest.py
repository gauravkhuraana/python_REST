import random
import pytest
from pytest_reportportal import RPLogger,RPLogHandler
from utils.file_reader import readFile



@pytest.fixture(scope="session")
def logger(request):
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)


    if hasattr(request.node.config,'py_test_service'):
        logging.setLoggerClass(RPLogger)
        rp_handler = RPLogHandler(request.node.config.py_test_service)

        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setLevel(logging.INFO)
        logger.addHandler(console_handler)
    else:
        rp_handler = logging.StreamHandler(sys.stdout)    

    rp_handler.setLevel(logging.INFO)    
    return logger




@pytest.fixture
def created_data():
    #obj=jsonOps()
    payload = readFile('createPerson.json')

    random_no= random.randint(0,1000)

    last_name = f'Olabini{random_no}'

    payload['lname']=last_name
    yield payload