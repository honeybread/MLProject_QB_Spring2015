# -*- coding: utf-8 -*-

import sqlite3, os
from matplotlib import pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages


class Exploration(object):
    def __init__(self):
        os.chdir('../../../data')
        self.conn = sqlite3.connect('quizbowl_buzz.db')
        self.cur = self.conn.cursor()
        self.pp = PdfPages('all_plots_corrected.pdf')
    
    def ques_per_cat(self):
        #query = "select category, count(*) as count from questions q JOIN train t ON q.id = t.question group by category order by count DESC "
	query = "select category, count(*) as count  from questions where id in (select distinct question from train) group by category order by count DESC "
        c = self.cur.execute(query,)
        data = c.fetchall()
        X = [z[0] for z in data]
        Y = [z[1] for z in data]
        plt.bar(range(len(Y)), Y, align='center')
        plt.xticks(range(len(X)), X, size='small', rotation='vertical')
        plt.title("Questions per Category", size = 'small')
        #plt.figure(figsize=(1.5,1.5))
	#plt.show()
	#print plt.figure.get_size_inches()
	#plt.savefig('plt.png',dpi=100)
        self.pp.savefig()
        plt.close()
        #self.pp.close()
        #plt.savefig(self.pp, format = 'pdf')
        
        print "\n\n"

    def user_per_cat(self):
        query = "select category, count(distinct user) as count from questions q JOIN train t ON q.id = t.question group by category order by count DESC "
        c = self.cur.execute(query,)
        data = c.fetchall()
        X = [z[0] for z in data]
        Y = [z[1] for z in data]
        plt.bar(range(len(Y)), Y, align='center')
        plt.xticks(range(len(X)), X, size='small', rotation='vertical')
        plt.title("Users per Category")
        #plt.show()
        plt.savefig(self.pp, format = 'pdf')
        #print c.fetchall()
        #self.pp.savefig()
        plt.close()
        #self.pp.close()
        print "\n\n"
        
    def cat_avg_buzz_pos(self):
        query = "select category, avg(abs(position)) as avg_buzz from questions q JOIN train t ON q.id = t.question group by category order by avg_buzz DESC "
        c = self.cur.execute(query,)
        data = c.fetchall()
        X = [z[0] for z in data]
        Y = [z[1] for z in data]
        plt.bar(range(len(Y)), Y, align='center')
        plt.xticks(range(len(X)), X, size='small', rotation='vertical')
        plt.title("Avg. Buzz position per Category")
        #plt.show()
        plt.savefig(self.pp, format = 'pdf')
        #print c.fetchall()
        #self.pp.savefig()
        plt.close()
        #self.pp.close()
        print "\n\n"
        
    def user_avg_buzz_pos(self):
        query = "select user, avg(abs(position)) as avg_buzz from questions q JOIN train t ON q.id = t.question group by user order by avg_buzz DESC"
        c = self.cur.execute(query,)
        data = c.fetchall()
        X = [z[0] for z in data]
        Y = [z[1] for z in data]
        plt.bar(range(len(Y)), Y, align='center')
        plt.xticks(range(len(X)), X, size='small', rotation='vertical')
	#plt.xlabel("Users")
        plt.title("Avg. Buzz position per User")
        #plt.show()
        plt.savefig(self.pp, format = 'pdf')
        #print c.fetchall()
        #self.pp.savefig()
        plt.close()
        #self.pp.close()
        print "\n\n"
        
    def cat_correctness_ratio(self):
        query = "select category, (sum(CASE WHEN position > 0 THEN 1.0 ELSE 0.0 END)/count(t.question)) as cor_ratio from questions q JOIN train t ON q.id = t.question group by category order by cor_ratio DESC "
        c = self.cur.execute(query,)
        data = c.fetchall()
        X = [z[0] for z in data]
        Y = [z[1] for z in data]
        plt.bar(range(len(Y)), Y, align='center')
        plt.xticks(range(len(X)), X, size='small', rotation='vertical')
        plt.title("Correctness ratio per Category")
        #plt.show()
        plt.savefig(self.pp, format = 'pdf')
        #print c.fetchall()
        #self.pp.savefig()
        self.pp.close()
        plt.close()
        print "\n\n"
        
if __name__ == "__main__":
    e = Exploration()
    e.ques_per_cat()
    e.user_per_cat()
    e.cat_avg_buzz_pos()
    e.user_avg_buzz_pos()
    e.cat_correctness_ratio()
