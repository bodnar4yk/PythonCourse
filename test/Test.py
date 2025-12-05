###Tak1###
# import unittest

# def multiply(a,b):
#     return a*b

# class TestMultiply(unittest.TestCase):
 
#     def testmultiply(self):
#         self.assertEqual(multiply(2,3),6)
#         self.assertEqual(multiply(3,3),9)
#         self.assertEqual(multiply(4,3),12)

# if __name__=="__main__":
#     unittest.main()

###Task2###
# from unittest.mock import Mock
# import unittest
# class TestMockExample(unittest.TestCase):
#     def test_mock(self):
#         mock = Mock()
#         mock.some_method.return_value = "mocked result"
#         result = mock.some_method()
#         self.assertEqual(result, "mocked результат")
# if __name__ == '__main__':
#     unittest.main()

###Task3###
# from unittest.mock import Mock
# import unittest
# def divide (a,b):
#     if b==0:
#         print("devide inpossible")
#     else:
#         return a/b

# class TestMockExample(unittest.TestCase):
#     def test_divide(self):
#         mock = Mock(side_effect=divide)
#         result = mock(10,2)
#         self.assertEqual(result,5)
#         self.assert_called_with(10,2)
        
# if __name__ == '__main__':
#     unittest.main()

###Task4###
from unittest.mock import patch
from unittest.mock import Mock
import unittest
import requests

def fetch_data(url):
    response = requests.get(url)
    return response.json()

class TestFetchData(unittest.TestCase):
    @patch('requests.get')
    def test_fetch_data(self, mock_get):
        mock_response = Mock()
        mock_response.json.return_value = {"key": "value"}
        mock_get.return_value = mock_response
        result = fetch_data("<http://example.com/api>")
        self.assertEqual(result, {"key": "value"})
        mock_get.assert_called_with("<http://example.com/api>")
if __name__ == '__main__':
    unittest.main()
