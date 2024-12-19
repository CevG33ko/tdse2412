import unittest


class TestMyModule(unittest.TestCase):
    def test_import(self):
        try:
            import tdse24gc
        except ImportError:
            self.fail("Importing mymodule failed")


if __name__ == "__main__":
    unittest.main()
