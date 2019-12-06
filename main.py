from publisher import Publisher
publisher = Publisher()

payload = {
    'device_id': 'someId',
    'location': 'living room',
    'temperature': 22.4,
    'humidity': 55.6
}
publisher.publish_message(payload)

publisher.close()
