from kazoo.client import KazooClient

zk = KazooClient(hosts='10.249.2.36:2182')
zk.start()

lock_path = '/12_p/curatorLock'

# 获取锁节点列表
lock_list = zk.get_children(lock_path)

for lock_node in lock_list:
    node_path = lock_path + '/' + lock_node
    # 获取节点状态信息
    stat = zk.exists(node_path)
    # 判断节点是否存在且未被释放
    if stat and stat.czxid == stat.mzxid and stat.numChildren==0:
        print("stat:{}".format(stat))
        print("Deleted lock node: {}".format(node_path))
        zk.delete(node_path)

zk.stop()
