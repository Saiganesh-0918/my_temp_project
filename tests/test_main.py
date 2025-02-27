import unittest
import sys
from io import StringIO
from my_temp_project.main import main  # Ensure this import works

class TestMain(unittest.TestCase):
    def setUp(self):
        self.captured_output = StringIO()  
        sys.stdout = self.captured_output  

    def tearDown(self):
        sys.stdout = sys.__stdout__  # Reset stdout after test

    def test_main_output(self):
        main()  # Run main function
        output = self.captured_output.getvalue().strip()
        expected_output = "Making Jenkins without toml and docker file"  # Adjust this based on actual output
        self.assertEqual(output, expected_output)

if __name__ == "__main__":
        unittest.main()

