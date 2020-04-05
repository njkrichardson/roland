import logging
import unittest 
import os 
import sys
import time
import shutil

# Logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(levelname)s:%(name)s:%(message)s')
file_handler = logging.FileHandler('logs/file_handler_test.log')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

class TestFileRerouting(unittest.TestCase): 
    """
    Test the automatic routing of files out of a 'tracking directory' 
    into a 'destination'. 
    """
    def setUp(self): 
        pass
        # create a test file in a temporary directory 
        # test_file = open('tmp/test_file.txt', 'w') 
        # test_file.close() 

    def tearDown(self): 
        pass

    def test_downloads_00(self): 
        """
        Test that the file actually leaves the directory being tracked.
        """
        os.system("touch tmp/test_file.txt")
        # move the test file to the directory to be tracked 
        shutil.move('tmp/test_file.txt', f'{os.getcwd()}/tracking/test_file.txt')
        print(os.listdir('tmp'))
        print(os.listdir('tracking'))

        # wait a hot sec 
        time.sleep(0.15)

        # verify that the test file has been moved 
        self.assertNotIn('test_file.txt', os.listdir(f'{os.getcwd()}/tracking'))

    def test_downloads_01(self): 
        """
        Verify that the destination directory receives the file
        """ 
        # wait a hot sec 
        time.sleep(0.15)

        # verify that it's in the right place 
        logger.debug(f'{os.getcwd()}/destination')
        self.assertIn('test_file.txt', os.listdir(f'{os.getcwd()}/destination'))

if __name__=='__main__': 
    unittest.main() 
