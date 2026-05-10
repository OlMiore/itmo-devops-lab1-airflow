from pyspark import SparkConf
from pyspark.sql import SparkSession
from pyspark.sql.functions import sum as spark_sum


def main():
    conf = (
        SparkConf()
        .setAppName("Sum Numbers PySpark Job")
        .setMaster("spark://spark-master:7077")
    )

    spark = SparkSession.builder.config(conf=conf).getOrCreate()

    try:
        numbers = [(1,), (2,), (3,), (4,), (5,)]
        numbers_df = spark.createDataFrame(numbers, ["number"])
        result = numbers_df.select(spark_sum("number").alias("total")).collect()[0]["total"]

        print(f"Final Spark sum is: {result}")
    finally:
        spark.stop()


if __name__ == "__main__":
    main()
