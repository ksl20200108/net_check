# How to start?

1. Each miner should create their own wallet first, otherwise, they will not receive any reward for mining the block.

2. Remember to change conf.py

3. start the one has bootstrap host first.

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

把client除send外不必要的sleep（shake_loop里的）删去
添加了类似区块同步的交易同步机制，把TCP中recv能够接收的最大数据量改成原来的两倍

此版本出现没有同时进行两个线程的情况

python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.46860337626723036
