def hello(event, context):
    """Basic functionality"""
    return {"message": "It's alive!", "event": event}


def test_endpoint(event, context):
    """Invoke the endpoint with some sample data"""
    import boto3
    import ast

    abalone_stats = """
    M,0.35,0.265,0.09,0.2255,0.0995,0.0485,0.07
    M,0.35,0.265,0.09,0.2255,0.0995,0.0485,0.07
    M,0.44,0.365,0.125,0.516,0.2155,0.114,0.155
    I,0.33,0.255,0.08,0.205,0.0895,0.0395,0.055
    """
    endpoint_name = "inference-pipeline-ep-2019-12-02-21-58-33"
    runtime = boto3.Session().client(
        service_name="sagemaker-runtime", region_name="us-east-1"
    )

    response = runtime.invoke_endpoint(
        EndpointName=endpoint_name, ContentType="text/csv", Body=abalone_stats
    )

    # Decode using the utf-8 encoding, turn into string
    result = ast.literal_eval(response["Body"].read().decode("utf-8"))

    return result


def create_estimator(event, context):
    from sagemaker.sklearn.estimator import SKLearn

    # script_path = "sklearn_abalone_featurizer.py"

    # sklearn_preprocessor = SKLearn(
    #     entry_point=script_path, role=role, train_instance_type="ml.c4.xlarge"
    # )
    return "Alrighty then."
