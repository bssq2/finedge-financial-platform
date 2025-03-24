from pyspark.sql import SparkSession
from pyspark.sql.functions import year, month, sum

def run_batch_etl(input_path: str, output_path: str):
    spark = SparkSession.builder.appName("FinEdgeBatchETL").getOrCreate()
    df = spark.read.parquet(input_path)

    monthly = df.groupBy(
        year("date").alias("year"),
        month("date").alias("month")
    ).agg(sum("amount").alias("monthly_revenue"))

    monthly.write.mode("overwrite").parquet(output_path)
    spark.stop()