# from pyspark import pipelines as dp
# from pyspark.sql.functions import col, count, count_if
# from utilities import utils

# # This file defines a sample transformation.
# # Edit the sample below or add new transformations
# # using "+ Add" in the file browser.

# @dp.table
# def sample_aggregation_first_sdp_pipeline():
#     return (
#         spark.read.table("sample_users_first_sdp_pipeline")
#         .withColumn("valid_email", utils.is_valid_email(col("email")))
#         .groupBy(col("user_type"))
#         .agg(
#             count("user_id").alias("total_count"),
#             count_if("valid_email").alias("count_valid_emails")
#         )
#     )
