# Task on string
import logging

logging.basicConfig(filename='File.log', level=logging.INFO, format='%(asctime)s %(levelname)s %(name)s %(message)s')
s = "this is My First Python programming class and i am learNING python string and its function"


class String_task:
    def extract_string(self, s):
        '''This documentation for extracting string as per specified
           range using oops concept'''
        logging.info('We are started to extract string')
        self.s = s
        try:
            if len(s) == 0:
                logging.error('Empty string')
            else:
                str = s[::3]
                logging.info('Extracted string is %s:', str)
                return str
        except Exception as e:
            logging.exception(e)

    def reverse_string(self, s):
        ''' This method writes the str in reverse direction'''
        logging.info('writing string in reverse order without reverse function')
        self.s = s
        try:
            rev = s[::-1]
            logging.info('reversed string is{}'.format(rev))
            return rev
        except Exception:
            print(logging.exception)

    def upper_split(self, s):
        ''' This method writes whole str in upper case splits wrt space '''
        logging.info('writing str in upper case and splitting')
        self.s = s
        try:
            upp_split = s.upper().split(' ')
            logging.info('converted to upper case & splitted')
            return upp_split
        except Exception:
            print(logging.exception)

    def capitalize(self, s):
        ''' This method capitalizes the str'''
        logging.info('start capitalization')
        self.s = s
        try:
            cap = s.capitalize()
            logging.info('capitalized str')
            return cap
        except Exception:
            print(logging.exception)


obj1 = String_task()
a = obj1.extract_string(s)
b = obj1.reverse_string(s)
c = obj1.upper_split(s)
d = obj1.capitalize(s)
print(a)
print(b)
print(c)
print(d)