import os
import activities
import unittest
import tempfile


class ActivitiesTestCase(unittest.TestCase):

    def setUp(self):
        self.db_fd, activities.app.config['DATABASE'] = tempfile.mkstemp()
        activities.app.config['TESTING'] = True
        self.app = activities.app.test_client()
        with activities.app.app_context():
            activities.init_db()

    def tearDown(self):
        os.close(self.db_fd)
        os.unlink(activities.app.config['DATABASE'])

if __name__ == '__main__':
    unittest.main()
