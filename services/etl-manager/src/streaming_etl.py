from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json, col
from pyspark.sql.types import StructType, StructField, StringType, DoubleType

def start_stream_processing(kafka_bootstrap: str, topic: str):
    spark = SparkSession.builder.appName("FinEdgeStreamingETL").getOrCreate()

    schema = StructType([
        StructField("id", StringType()),
        StructField("total", DoubleType()),
        StructField("txn_date", StringType()),
    ])

    df = spark.readStream \
        .format("kafka") \
        .option("kafka.bootstrap.servers", kafka_bootstrap) \
        .option("subscribe", topic) \
        .load()

    parsed = df.select(from_json(col("value").cast("string"), schema).alias("data"))

    query = parsed.writeStream \
        .outputMode("append") \
        .format("console") \
        .start()

    query.awaitTermination()