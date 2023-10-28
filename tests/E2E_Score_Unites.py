
import unittest
from e2e import is_service_available


class E2E_Score_Unitest(unittest.TestCase):
    def test_selenium_action(self):
        if not is_service_available("http://localhost:30000/score") :
            self.fail("Selenium action failed: Element not found")


unittest.main()
