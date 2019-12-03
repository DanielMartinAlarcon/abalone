def hello(event, context):
    """Basic functionality"""
    return {"message": "It's alive!", "event": event}


def call_endpoint(event, context):
    """Process incoming CSV"""
    print(f"event: {event}")

    endpoint_name = "inference-pipeline-ep-2019-12-02-21-58-33"

    from sagemaker.predictor import (
        csv_serializer,
        json_deserializer,
        RealTimePredictor,
    )
    from sagemaker.content_types import CONTENT_TYPE_CSV, CONTENT_TYPE_JSON

    payload = "M, 0.35, 0.365, 0.125, 0.516, 0.2155, 0.114, 0.155"
    predictor = RealTimePredictor(
        endpoint=endpoint_name,
        #     sagemaker_session=sagemaker_session,
        serializer=csv_serializer,
        deserializer=json_deserializer,
        content_type=CONTENT_TYPE_CSV,
        accept=CONTENT_TYPE_JSON,
    )

    result = predictor.predict(payload)
    print(f"result: {result}")

    return result
