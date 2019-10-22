# -*-coding:utf-8-*-
# @auth ivan
# @time 20191022 03:13:11
# @goal Test Mrjob MapReduce

from mrjob.job import MRJob

class MRWordCounter(MRJob):
    def mapper(self,key,line):
        for word in line.split():
            yield word,1

    def reducer(self,word,occurrences):
        yield word,sum(occurrences)

if __name__ == '__main__':
    MRWordCounter.run()

