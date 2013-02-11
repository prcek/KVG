import unittest
import os
import sys

class Test(unittest.TestCase):
    def test_one(self):
        import main
        import webapp2
        request = webapp2.Request.blank('/')
        response = request.get_response(main.app)
        self.assertEqual(response.status_int, 200)
        

    
def run():
    sys.path.insert(0,'/usr/local/bin')
    import dev_appserver
    dev_appserver.fix_sys_path()
    suite = unittest.loader.TestLoader().discover(os.path.dirname(__file__))
    unittest.TextTestRunner(verbosity=2).run(suite) 




if __name__ == '__main__':
    run()

    