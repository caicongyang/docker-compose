from kazoo.client import KazooClient
from kazoo.exceptions import NoNodeError
import datetime

zk = KazooClient(hosts='192.168.0.1:2182')
zk.start()

today = datetime.date.today()
nodes = zk.get_children('/12_p/curatorLock')
nodes_to_delete = [node for node in nodes if node < today.isoformat()]

for node in nodes_to_delete:
    node_path = '/12_p/curatorLock/' + node
    try:
        print("delete node:{}".format(node_path))
        zk.delete_async(node_path).get()
    except NoNodeError:
        pass

zk.stop()