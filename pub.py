"""
export GOOGLE_APPLICATION_CREDENTIALS="/home/user/Downloads/[FILE_NAME].json"
"""

from google.cloud import pubsub_v1
import json

project_id = "henofs-project"
topic_name = "sensor-data"

publisher = pubsub_v1.PublisherClient()
# The `topic_path` method creates a fully qualified identifier
# in the form `projects/{project_id}/topics/{topic_name}`
topic_path = publisher.topic_path(project_id, topic_name)

payload = {
    "test": 100,
    "device": "some device"
}

data = json.dumps(payload).encode('utf-8')

# When you publish a message, the client returns a future.
future = publisher.publish(topic_path, data=data)
print(future.result())

print('Published messages.')