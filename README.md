 # RFM ile Müşteri Segmentasyonu (Customer Segmentation with RFM)

This repository contains code and data for customer segmentation using the RFM (Recency, Frequency, Monetary) analysis. The goal is to divide FLO's customers into segments and determine marketing strategies based on these segments.

## Dataset

The dataset consists of historical shopping behavior data of customers who made their last purchases through OmniChannel (both online and offline) channels between 2020 and 2021. It includes information such as customer IDs, order channels, order dates, total order numbers, total customer value, and interested categories.

## Business Problem

FLO wants to divide its customers into segments and develop marketing strategies accordingly. The customers' behaviors will be defined, and groups will be created based on these behavior patterns.

## Tasks

### Task 1: Data Preparation and Understanding

- Read and load the "flo_data_20k.csv" dataset.
- Perform data exploration tasks:
  - Display the first 10 observations.
  - List the variable names.
  - Examine the dataset dimensions.
  - Calculate descriptive statistics.
  - Identify missing values.
  - Analyze variable types and convert date variables to the date format.
- Create new variables to capture the total order numbers and total customer value for omnichannel customers.
- Functionally convert date variables to the datetime format.

### Task 2: Calculating RFM Metrics

- Calculate the Recency, Frequency, and Monetary metrics based on the dataset.
- Calculate the RF scores for each customer.

### Task 3: Calculating RFM Scores and Defining Segments

- Convert the RF scores into more understandable segments using segment mapping.
- Assign RFM scores and segments to each customer.

### Task 4: Analyzing Segment Characteristics

- Analyze the average Recency, Frequency, and Monetary values for each segment.

### Task 5: Taking Action

- Analyze segment characteristics to identify target customer profiles.
- For two specific cases:
  - Identify customers who are loyal, interested in the women's category, and have an average customer value greater than 250 TL. Save their IDs to a CSV file named "yeni_marka_hedef_musteri.csv".
  - Identify customers who are potentially interested in the men's and children's categories and fall into specific segments (hibernating, can't lose, new customers). Save their IDs to a CSV file named "indirim_hedef_müşteri_ids.csv".

### Task 6: Functionality

- Functionally encapsulate the entire process.

Please note that this is a summary of the code and its tasks. For a more detailed explanation and code implementation, please refer to the provided code file.

