from app import app
import unittest


class FlaskTestCase(unittest.TestCase):

    #test loading index page
    def test_index(self):
        tester = app.test_client(self)
        response = tester.get('/login', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    #test login page loads correctly
    def test_login_page_loads(self):
        tester = app.test_client(self)
        response = tester.get('/login', content_type='html/text')
        self.assertTrue(u'Login' in response.data)

    #test login page behave correctly given the correct credentials
    def test_correct_login(self):
        tester = app.test_client(self)
        response = tester.post('/login',
                               data=dict(username='admin', password='admin'),
                               follow_redirects=True)
        self.assertIn(u'You were just logged in!', response.data)

    #test login page behave correctly given the incorrect credentials
    def test_incorrect_login(self):
        tester = app.test_client(self)
        response = tester.post('/login',
                               data=dict(username='a123', password='12345'),
                               follow_redirects=True)
        self.assertIn(u'Incorrect username or password. Please try again!', response.data)

    #test logout page behave correctly
    def test_logout(self):
        tester = app.test_client(self)
        tester.post('/login', data=dict(username='admin', password='admin'),
                    follow_redirects=True)
        response = tester.get('/logout', follow_redirects=True)
        self.assertIn(u'You were just logged out!', response.data)


if __name__ == '__main__':
    unittest.main()