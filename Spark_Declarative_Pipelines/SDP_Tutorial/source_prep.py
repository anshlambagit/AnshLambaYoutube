# Databricks notebook source
# MAGIC %sql
# MAGIC -- CREATE TABLE sdp_catalog.source.sales 
# MAGIC -- (
# MAGIC --   order_id INT, 
# MAGIC --   product_id INT, 
# MAGIC --   revenue FLOAT,
# MAGIC --   date DATE,
# MAGIC --   store_id INT
# MAGIC -- );
# MAGIC
# MAGIC INSERT INTO sdp_catalog.source.sales 
# MAGIC VALUES 
# MAGIC (7, 1001, 100.00, '2022-01-01', 1),
# MAGIC (8, 1002, 200.00, '2022-01-02', 2)
# MAGIC -- (3, 1003, 300.00, '2022-01-03', 3),
# MAGIC -- (4, 1004, 400.00, '2022-01-04', 4);

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT * FROM sdp_catalog.source.sales;

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT * FROM sdp_catalog.target.cur_sales_stream

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE TABLE sdp_catalog.source.sales_north 
# MAGIC (
# MAGIC   order_id INT, 
# MAGIC   product_id INT, 
# MAGIC   revenue FLOAT,
# MAGIC   date DATE,
# MAGIC   store_id INT
# MAGIC );
# MAGIC
# MAGIC INSERT INTO sdp_catalog.source.sales_north 
# MAGIC VALUES 
# MAGIC (1, 1001, 100.00, '2022-01-01', 1),
# MAGIC (2, 1002, 200.00, '2022-01-02', 2),
# MAGIC (3, 1003, 300.00, '2022-01-03', 3),
# MAGIC (4, 1004, 400.00, '2022-01-04', 4);
# MAGIC
# MAGIC
# MAGIC CREATE TABLE sdp_catalog.source.sales_south
# MAGIC (
# MAGIC   order_id INT, 
# MAGIC   product_id INT, 
# MAGIC   revenue FLOAT,
# MAGIC   date DATE,
# MAGIC   store_id INT
# MAGIC );
# MAGIC
# MAGIC INSERT INTO sdp_catalog.source.sales_south
# MAGIC VALUES 
# MAGIC (5, 1001, 100.00, '2022-01-01', 1),
# MAGIC (6, 1002, 200.00, '2022-01-02', 2),
# MAGIC (7, 1003, 300.00, '2022-01-03', 3),
# MAGIC (8, 1004, 400.00, '2022-01-04', 4);

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT * FROM sdp_catalog.target.total_sales

# COMMAND ----------

# MAGIC %md
# MAGIC ### **SLOWLY CHANGING DIMS**

# COMMAND ----------

# MAGIC %sql
# MAGIC -- CREATE TABLE sdp_catalog.source.products 
# MAGIC -- (
# MAGIC --   product_id INT, 
# MAGIC --   product_name STRING, 
# MAGIC --   category STRING,
# MAGIC --   subcategory STRING,
# MAGIC --   updated_at TIMESTAMP
# MAGIC -- );
# MAGIC
# MAGIC INSERT INTO sdp_catalog.source.products 
# MAGIC VALUES 
# MAGIC -- (1001, 'Product1', 'Category1', 'Subcategory1', current_timestamp()),
# MAGIC -- (1002, 'Product2', 'Category2', 'Subcategory2', current_timestamp()),
# MAGIC (null, 'Product3', 'Category4', 'Subcategory4', current_timestamp());
# MAGIC -- (1004, 'Product4', 'Category4', 'Subcategory4', current_timestamp()); 
# MAGIC
# MAGIC SELECT * FROM sdp_catalog.source.products;

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT * FROM sdp_catalog.target.products_scd1

# COMMAND ----------

