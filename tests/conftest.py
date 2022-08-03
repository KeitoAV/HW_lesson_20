import time

import pytest


@pytest.fixture(autouse=True, scope='class')
def time_after_class_tests():
    yield
    now = time.time()
    print('\n-----')
    print("each class finished : {}".format(time.strftime('%d %b %X', time.localtime(now))))
    print('-----------------')

# pytest -s
# pytest --setup-show -v
