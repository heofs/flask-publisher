"""
export GOOGLE_APPLICATION_CREDENTIALS="/home/user/Downloads/[FILE_NAME].json"
"""

from google.cloud import pubsub_v1
import json


class Publisher(object):
    def __init__(self, project_id="henofs-project", topic_name="sensor-data"):
        self.publisher = pubsub_v1.PublisherClient()

        # The `topic_path` method creates a fully qualified identifier
        # in the form `projects/{project_id}/topics/{topic_name}`
        self.topic_path = self.publisher.topic_path(project_id, topic_name)

    def publish_data(self, data={"test": 100}):
        data = json.dumps(data).encode('utf-8')

        # When you publish a message, the client returns a future.
        future = self.publisher.publish(self.topic_path, data=data)

        return future.result()


if __name__ == "__main__":
    publisher = Publisher()
    publisher.publish_data()

    print('Published messages.')
