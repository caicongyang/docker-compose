from kazoo.client import KazooClient

zk = KazooClient(hosts='127.0.0.1:2181')
zk.start()

def check_ephemeral_node(path):
    data, stat = zk.get(path)
    if stat.ephemeralOwner != 0 and not zk.exists(path, watch=None):
        print("Ephemeral node %s has expired" % path)
        zk.delete(path)

def check_children(path):
    children = zk.get_children(path)
    for child in children:
        child_path = path + "/" + child
        check_ephemeral_node(child_path)
        check_children(child_path)

check_children("/12_p/curatorLock")