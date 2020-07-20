# How to start?

1. Each miner should create their own wallet first, otherwise, they will not receive any reward for mining the block.

2. Remember to change conf.py

# Sketches:

1. Include a transaction in block if its fee is higher than 0.1.

2. 1 tx per block and 1 minute per block

3. No tx time limit:

4. Model ends after 11-th block

5. 10 miners
11 users

6. Each user generates 1 transaction with transaction fees which follow uniform distribution

# Changes:

experiment1: network, txpool

# Tips

You should know that there are some differences between machines and computers as well as network environment. I have SPENT A LOT OF WEEKS dealing with the problems caused by these differences. It is really frustrated and I find sometimes a tiny difference may make some part in the code fail. However, the CODE DO WORK IN SOME ENVIRONMENT AND MACHINES. So if the code does not work on your computer, you should try to find the problem yourself. May be the network on your machine have some problem. Try the "ping" and use "telnet" to check that whether the the port 5678 and 5984 can be visited. And somehow change the code yourself to make it adapt to your environment when it is necessary.

Also, it is suggested that you should consider to use a machine with stable performence.

# 笔记
着手解决E1.3 README中提到的问题
加入多条日志，发现由于广播方式有问题（只由产生交易的机子广播一遍，无法通知暂时失联的节点）

改为比特币的广播模式，节点收到交易后再次广播，每个节点收到交易后在handle_transaction中遍历区块交易，判断是否将交易纳入交易池
（之后数据量大的话需要从存储入手，在数据库里存储交易所在区块的信息）
