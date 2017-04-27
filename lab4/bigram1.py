from __future__ import print_function

import sys
from operator import add
from pyspark import SparkContext


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: bigram <file>", file=sys.stderr)
        exit(-1)
    sc = SparkContext()
    lines = sc.textFile(sys.argv[1], 1)
    sentences = lines.glom() \
                  .map(lambda x: " ".join(x)) \
                  .flatMap(lambda x: x.split("."))

    #Your code goes here
    bigram=sentences.map(lambda x:x.split()) \
                                .flatMap(lambda x: [((x[i],x[i+1]),1) for i in range(0,len(x)-1)])
    freq_bigrams = bigram.reduceByKey(lambda x,y:x+y) \
                                      .sortBy(lambda x: x[1],False)
    sort100=freq_bigrams.take(100)
    sc.parallelize(sort100).saveAsTextFile('top100.out')
                    



    sc.stop()
