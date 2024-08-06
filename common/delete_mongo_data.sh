#!/bin/bash

CONNECTION_STRING="mongodb://root:root@127.0.0.1:27017/test"

# 执行删除操作
mongosh "$CONNECTION_STRING" --eval "db.test1.remove({});db.test2.remove({});"
