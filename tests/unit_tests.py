import unittest

import flask_app as app

class TestApp(unittest.TestCase):
    def test_load_user(self):
        """It should:
        1. Return a db instance of the correct user if exists
        2. Return None if does not exist"""

        user = app.load_user(1)
        self.assertEqual(user.id, 1)

        user = app.load_user(0)
        self.assertTrue(user is None)


if __name__ == '__main__':
    unittest.main()
