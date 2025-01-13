from google.transit import gtfs_realtime_pb2
from google.protobuf.json_format import MessageToDict
import requests
import json

downeasters = [680, 690, 682, 692, 684, 694, 686, 696, 688, 698, 681, 691, 683, 693, 687, 697, 689, 699, 1689]
downeasters = [680, 681, 682, 683, 684, 686, 687, 688, 689, 690, 691, 692, 693, 694, 696, 697, 698, 699, 1689]

feed = gtfs_realtime_pb2.FeedMessage()
response = requests.get('https://asm-backend.transitdocs.com/gtfs/amtrak')
feed.ParseFromString(response.content)

for entity in feed.entity:
  if entity.HasField('trip_update'):
    dicto = MessageToDict(entity)

    train_num = 0

    try:
        train_num = int(dicto['id'].split("_")[-1])
    except:
        print("Failed to parse" + dicto["id"])

    if train_num in downeasters:
        print(json.dumps(dicto, sort_keys=True, indent=4))
    