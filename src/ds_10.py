
import pyspark
myConf=pyspark.SparkConf()

spark = pyspark.sql.SparkSession.builder.master("local").appName("myApp").config(conf=myConf).getOrCreate()
Rdd = spark.sparkContext.textFile(os.path.join('data','ds_spark_wiki.txt'));

wc=Rdd.flatMap(lambda x:x.split()).map(lambda x:(x,1)).reduceByKey(lambda x,y:x+y).map(lambda x:(x[1],x[0])).sortByKey(False).take(10)
print type(wc)
for i in wc:
    print i