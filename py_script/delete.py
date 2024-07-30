from kazoo.client import KazooClient
import datetime

zk = KazooClient(hosts='192.168.0.1:2182')
zk.start()
root="/12_p/curatorLock"

today = datetime.date.today()
nodes = zk.get_children(root)
nodes_to_delete = []

for node in nodes:
    node_path = root+"/"+ node
    node_stat = zk.exists(node_path)
    if node_stat is None:
        continue
    node_ctime = datetime.datetime.fromtimestamp(node_stat.ctime / 1000)
    node_mtime = datetime.datetime.fromtimestamp(node_stat.mtime / 1000)
    if node_ctime.date() < today and node_ctime == node_mtime and node_stat.numChildren==0:
        print("delete node:{}".format(node_path))
        zk.delete(node_path)

zk.stop()