import os
CLIENT_A="c220g1-030822.wisc.cloudlab.us"
SERVER="c220g1-030827.wisc.cloudlab.us"
CLIENT_B="c220g1-030825.wisc.cloudlab.us"
MOUNT_POINT="/tmp/wowfs"

TEST_DATA_DIR = MOUNT_POINT + '/test_consistency'
TEST_SCRIPT_DIR = f"{os.path.expanduser('~')}/wow-so-distributed/workloads/consistency_tests/tests"
TEST_CASE_NO = 6
FNAME = f'{TEST_DATA_DIR}/case{TEST_CASE_NO}'

server_signal = "/tmp/WAKEUP_SERVER"
b_signal = "/tmp/WAKEUP_B"
