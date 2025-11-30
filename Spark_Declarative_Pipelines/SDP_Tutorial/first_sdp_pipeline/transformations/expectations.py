# from pyspark import pipelines as dp
# from pyspark.sql.functions import * 


# rules = {"rule1":"product_id IS NOT NULL",
#          "rule2":"updated_at is NOT NULL"}


# @dp.table(name="products_table")
# @dp.expect_all_or_fail(rules)
# def products_table():
#   df = spark.read.table("sdp_catalog.source.products")
#   return df


