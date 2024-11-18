from googleapiclient.discovery import build


def trigger_df_job(cloud_event,environment):   
 
    service = build('dataflow', 'v1b3')
    project = "adroit-autumn-440412-g7"

    template_path = "gs://dataflow-templates-us-central1/latest/GCS_Text_to_BigQuery"

    template_body = {
        "jobName": "bq-load",  # Provide a unique name for the job
        "parameters": {
        "javascriptTextTransformGcsPath": "gs://dataflow_metadata_demo/udf.js",
        "JSONPath": "gs://dataflow_metadata_demo/BQ.json",
        "javascriptTextTransformFunctionName": "transform",
        "outputTable": "adroit-autumn-440412-g7:circket_dataset.icc_cricket_ranking",
        "inputFilePattern": "gs://cricket-batting-ranking-data/batsmen_rankings.csv",
        "bigQueryLoadingTemporaryDirectory": "gs://dataflow_metadata_demo/temp",
        }
    }

    request = service.projects().templates().launch(projectId=project,gcsPath=template_path, body=template_body)
    response = request.execute()
    print(response)