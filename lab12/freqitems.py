from __future__ import print_function

import sys
from operator import add

from pyspark import SparkContext
from pyspark.mllib.fpm import FPGrowth


if __name__ == "__main__":
    sc = SparkContext(appName="FreqItems")
    data = sc.textFile(sys.argv[1])
    transactions = data.map(lambda line: line.strip().split(','))
    model = FPGrowth.train(transactions, minSupport=0.02, numPartitions=10)
    model = model.freqItemsets()
    #results=model.collect()
    model=model.filter(lambda x:len(x[0])>=2)
    results=model.sortBy(lambda x: x[1],False).collect()
    for line in results:
    	#if line
        print("%s" % (str(line)))

    sc.stop()
