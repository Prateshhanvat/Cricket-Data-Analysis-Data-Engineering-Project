# Cricket-Data-Analysis-Data-Engineering-Project
In Data Engineering, the process of transforming raw data into meaningful visual insights is both challenging and rewarding. This guide takes you through the detailed steps of building a robust cricket statistics pipeline with Google Cloud services. From fetching data through the Cricbuzz API to loading data into Big Query for visualization, each stage plays a vital role in ensuring a smooth data flow for analysis and visualization.




# Data Retrieval with Python and Cricbuzz API : -
The foundation of our project begins with Python’s prowess in interfacing with APIs. We’ll delve into the methods of fetching cricket statistics from the Cricbuzz API, harnessing the power of Python to gather the required data efficiently.
# Storing Data in Google Cloud Storage (GCS) :-
Once the data is obtained, our next step involves preserving it securely in the cloud. We’ll explore how to store this data in a CSV format within Google Cloud Storage (GCS), ensuring accessibility and scalability for future processing.
# Creating a Cloud Function Trigger :- 
With our data safely stored, we proceed to set up a Cloud Function that acts as the catalyst for our pipeline. This function triggers upon file upload to the GCS bucket, serving as the initiator for our subsequent data processing steps.
# Execution of the Cloud Function : - 
Within the Cloud Function, intricate code is crafted to precisely trigger a Dataflow job. We’ll meticulously handle triggers and pass the requisite parameters to seamlessly initiate the Dataflow job, ensuring a smooth flow of data processing.
# Dataflow Job for BigQuery :- 
The core of our pipeline lies in the Dataflow job. Triggered by the Cloud Function, this job orchestrates the transfer of data from the CSV file in GCS to BigQuery. We’ll meticulously configure the job settings to ensure optimal performance and accurate data ingestion into BigQuery.
