import unittest
import lambdaFunction.lambda_square_function as lambda_function
import json


class TestHandlerCase(unittest.TestCase):
    def setUp(self):
        pass
    
    def tearDown(self):
        pass
    
    def test_response(self):
        """assert correct output is given for a valid input"""
        event={'input':5}
        result = lambda_function.lambda_square_handler(event, None)
        result_body = json.loads(result['body'])
        
        print(type(result['body']))
        self.assertEqual(result_body['output'], 25) # did we get the result we expected?
        # self.assertEqual(result['headers']['Content-Type'], 'application/json') # does the function return the datatype?
    
    def test_response_wrong_input_type(self):
        """assert error is thrown if wrong input type provided"""
        event={'input':'a'}
        with self.assertRaises(Exception): lambda_function.lambda_square_handler(event, None)

if __name__ == '__main__':
    unittest.main()
