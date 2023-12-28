import asyncio
from pyzeebe import (
    ZeebeClient,
    create_camunda_cloud_channel,
)

async def main():
    # Create a Zeebe client for Camunda Cloud
    grpc_channel = create_camunda_cloud_channel(
        client_id="<CLIENT-ID>",
        client_secret="CLIENT-SECRET",
        cluster_id="<CLUSTER-ID>",
        region="bru-2",  # Default is bru-2
    )
    zeebe_client = ZeebeClient(grpc_channel)

    camunda_var = {
        "awsDeploymentSuccessful": True
    }

    # Publish message
    await zeebe_client.publish_message(name="sqsOrderId", correlation_key="<ORDER-ID>", variables=camunda_var)

# Run the asynchronous main function
asyncio.run(main())