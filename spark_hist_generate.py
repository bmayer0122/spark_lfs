from pyspark import SparkContext

logFile = "~/projects/spark/histogram/README.md" 

# Create Spark context
sc = SparkContext("local", "Histogram")
logData = sc.textFile(logFile).cache()

# Generte data
nums = sc.parallelize(range(0,10))
oversample = nums.sample(True, 1000)

# Open file and write histogram
f = open('histogram.txt', 'w')
f.write(str(oversample.histogram(range(0,11))))
f.close()
