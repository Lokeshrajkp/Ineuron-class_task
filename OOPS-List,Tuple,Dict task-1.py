import logging

logging.basicConfig(filename='File.log', level=logging.INFO, format='%(asctime)s %(levelname)s %(name)s %(message)s')


class List:
    def __init__(self, collection):
        self.collection = collection

    def extract_list(self):
        ''' This method performs extracting list from the collection'''
        try:
            logging.info('extracting list from collection')
            for i in self.collection:
                if type(i) == list:
                    print(i)
            logging.info('extracting tuple is completed')
        except Exception as e:
            logging.exception(e)

    def extract_tuple(self):
        ''' This method performs extracting tuple from the collection'''
        try:
            logging.info('extracting tuple from collection')
            for i in self.collection:
                if type(i) == tuple:
                    print(i)
            logging.info('extracting tuple is completed')
        except Exception as e:
            logging.exception(e)

    def extract_dict(self):
        ''' This method performs extracting dict from the collection'''
        try:
            logging.info('extracting dict from collection')
            for i in self.collection:
                if type(i) == dict:
                    print(i)
            logging.info('extracting dict is completed')
        except Exception as e:
            logging.exception(e)

    def extract_numdata(self):
        ''' This method performs extracting number from the collection'''
        try:
            logging.info('extracting num from collection')
            l1 = []
            for i in self.collection:
                if type(i) == list or type(i) == tuple or type(i) == set:
                    for j in i:
                        if type(j) == int:
                            l1.append(j)
                if type(i) == dict:
                    for k in i.items():
                        for g in k:
                            if type(g) == int:
                                l1.append(g)
            return l1

            logging.info('extracting num is completed')
        except Exception as e:
            logging.exception(e)


l = [[1, 2, 3, 4], (2, 3, 4, 5, 6), (3, 4, 5, 6, 7), set([23, 4, 5, 45, 4, 4, 5, 45, 45, 4, 5]),
     {'k1': "sudh", "k2": "ineuron", "k3":
         "kumar", 3: 6, 7: 8}, ["ineuron", "data science "]]
obj = List(l)
obj.extract_list()
obj.extract_tuple()
obj.extract_dict()
obj.extract_numdata()