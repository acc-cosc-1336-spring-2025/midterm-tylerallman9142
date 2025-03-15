#write function tests here, don't add input('') statements here!
import unittest

#follow this example to add questions b, c, and d for testing including their functions
from src.question_a.question_a import test_config, global_var, use_global
from src.question_b.question_b import get_fahrenheit
from src.question_c.question_c import get_bonus_pay_amount
from src.question_d.question_d import get_day_of_week

class Test_Config(unittest.TestCase):

    def test_question_a_config(self):
        self.assertEqual(True, test_config())

    def test_global_variable(self):
        global global_var
        initial_value = global_var
        use_global()
        self.assertEqual(global_var, initial_value + 5, "Global variable was not modified correctly")

    def test_get_fahrenheit(self):
        self.assertEqual(get_fahrenheit(0), 32, "0°C should be 32°F")
        self.assertEqual(get_fahrenheit(5), 41, "5°C should be 41°F")
        self.assertEqual(get_fahrenheit(10), 50, "10°C should be 50°F")

    def test_get_bonus_pay_amount(self):
        self.assertEqual(get_bonus_pay_amount(-1), "Invalid Arguments")
        self.assertEqual(get_bonus_pay_amount(200), 10)
        self.assertEqual(get_bonus_pay_amount(600), 36)
        self.assertEqual(get_bonus_pay_amount(1000), 70)
        self.assertEqual(get_bonus_pay_amount(1500), 120)
        self.assertEqual(get_bonus_pay_amount(2000), "Invalid Arguments")

    def test_get_day_of_week(self):
        self.assertEqual(get_day_of_week(0), "Invalid number")
        self.assertEqual(get_day_of_week(1), "Monday")
        self.assertEqual(get_day_of_week(2), "Tuesday")
        self.assertEqual(get_day_of_week(3), "Wednesday")
        self.assertEqual(get_day_of_week(8), "Invalid number")


