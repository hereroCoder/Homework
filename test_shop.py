# Write at least 5 unit tests in total covering various and appropriate cases.
from unittest import TestCase, main
from unittest.mock import patch
from shop import  shopping_attempts, can_afford, NoEnoughIncomeError

class TestShoppingAttempts(TestCase):

    def setUp(self):
        self.price = 2
        self.customer_money = 10
        self.items ={'cup':5, 'spoon':2}


    #testing if customer can exit if they input e
    string_input = 'e' 
    @patch('builtins.input', return_value=string_input)
    def test_customer_leaving(self, mock_input):
        result = shopping_attempts(self.items, self.customer_money,0)
        self.assertEqual(result,None)
      

    # testing if value error is raised for invalid option
    string_input = 'nike'
    @patch('builtins.input', return_value=string_input)
    def test_invalid_option(self,mock_input):
        self.assertRaises(ValueError, shopping_attempts, self.items, self.customer_money,0)
       

    #testing if customer gets item and exit if they can afford
    string_input = 'spoon'
    @patch('builtins.input', return_value=string_input)
    def test_customer_bought_item(self, mock_input):
        result = shopping_attempts(self.items, self.customer_money,0)
        self.assertEqual(result, None)
        

    # testing if customer can afford
    def test_can_afford(self):
       result = can_afford(self.price, self.customer_money)
       if self.price < self.customer_money:
            self.assertTrue(result)
       else:
            self.assertFalse(result)

    # testing if custom error raised after 3 attempts
    string_input = 'cup'
    @patch('builtins.input', return_value=string_input)
    def test_customer_error_raised(self, mock_input):
        self.assertRaises(NoEnoughIncomeError, shopping_attempts,
                           self.items, self.customer_money, 4)


if __name__ == '__main__':
    main()
