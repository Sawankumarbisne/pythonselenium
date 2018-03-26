from unittest import TestLoader, TestSuite, TextTestRunner
from Test.PageObject.Scripts.LoginPage import LoginPage

if __name__ == "__main__":

    loader = TestLoader()
    suite = TestSuite((
        loader.loadTestsFromTestCase(LoginPage),
               ))

#run test sequentially using simple TextTestRunner
    runner = TextTestRunner(verbosity=2)
    runner.run(suite)


# #run test parallel using concurrent_suite
