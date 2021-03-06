# -*- coding: utf-8 -*-
import sqlite3, sys
import cPickle as pickle
import argparse

class StanfordParser(object):
    '''class to dependency parse question text using Stanford Parser'''
    def __init__(self, parser_path, parser_dir):
        self.parser_path = parser_path
        self.parser_dir = parser_dir
        
        sys.path.append(self.parser_path)
        from corenlp import StanfordCoreNLP
        self.parser = StanfordCoreNLP(self.parser_path + self.parser_dir)
        
    def parser(self, qtext):
        return self.raw_parse(qtext)
        
        

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description= "k")
    parser.add_argument("--parser_path", default = '../../../../corenlp-python/', help = \
    "Path that points to Stanford Parser")
    parser.add_argument("--parser_dir_name", default = 'stanford-corenlp-full-2014-08-27', help = \
    "Name of directory containing Stanford Parser")
    parser.add_argument("--db_path", default = '../../../data/quizbowl_buzz.db', help = \
    "Path that points to DB containing Quiz Bowl data")
    
    flags = parser.parse_args()
    
    conn = sqlite3.connect(flags.db_path)
    cur = conn.cursor()
    s = StanfordParser(flags.parser_path, flags.parser_dir_name)
    
    query = "select id, text from questions"
    c = cur.execute(query,)
    all_questions =  c.fetchall()
    
    print "questions fetched"
    pointer_id = 152
    print "started"
    count = pointer_id
    passed_ids = []
    
    with open("/Users/manjhunathkr/Documents/MLProject_Home/data/stanford_parse_dump.txt", "a") as fp:
        for ID, qtext in all_questions:
            if ID < pointer_id:
                continue
            try:
                sparse_output = {}
                sparse = s.parser.raw_parse(qtext)
                print count
                sparse_output.update({ID: sparse})
                count += 1
                pickle.dump(sparse_output, fp)
            except:
                passed_ids.append(ID)
                pass

        