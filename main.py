# -*- coding: UTF-8 -*-
from uitrace.api import *
from test_secure_fix import *

init_driver(workspace=os.path.dirname(__file__))
# TODO: write your code
cmd_adb("shell pm clear com.tencent.qqpimsecure", id_mark=True, timeout=-1)

test_fix_quick()
if __name__ == '__main__':
    pytest.main()


stop_driver()
