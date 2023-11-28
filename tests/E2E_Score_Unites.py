
import unittest
from e2e import is_service_available,validate_user_score_with_limits
class E2E_Score_Unitest(unittest.TestCase):
    def test_score_service(self):
        if not is_service_available("http://localhost:8777") :
            self.fail("Selenium action failed: Element not found")
            
    def test_user_score_with_limits(self):
        if not validate_user_score_with_limits("http://localhost:8777","idubi",1,1000) :
            self.fail("Selenium action failed: Element not found")
            




unittest.main()
