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

experiment1: packing

# Tips

You should know that there are some differences between machines and computers as well as network environment. I have SPENT A LOT OF WEEKS dealing with the problems caused by these differences. It is really frustrated and I find sometimes a tiny difference may make some part in the code fail. However, the CODE DO WORK IN SOME ENVIRONMENT AND MACHINES. So if the code does not work on your computer, you should try to find the problem yourself. May be the network on your machine have some problem. Try the "ping" and use "telnet" to check that whether the the port 5678 and 5984 can be visited. And somehow change the code yourself to make it adapt to your environment when it is necessary.

Also, it is suggested that you should consider to use a machine with stable performence.

# 笔记
此版本在十八台Linux机器上运行，能够同时调用client和server内的函数，各节点日志刷新正常，解决了突然卡顿的问题（通过在server的handle_loop内判断recv函数值，判断连接是否中断并决定是否结束进程，暂时认为not recv是连接中断的标志）。但是解决了handle_loop死循环的问题后，失联的节点通常进入peerserver中寻找节点的死循环。

再者交易广播有问题，发现发送交易的机子虽然在十七个peerserver中的client添加交易（add_tx），但是日志显示最终client只发送出了两条交易信息，也就是只向两个节点发送了交易信息。
