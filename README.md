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

此版本意在解决不能同时运行两个线程的情况

python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 




experiment 1
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.418995
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.513541
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.191829
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.379950
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.161266
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.566069
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.551672
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.347644
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.136812
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.470063

experiment 2
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.489420
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.303687
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.231089
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.250302
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.427685
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.316344
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.466592
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.498466
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.287185
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.499343

experiment 3
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.207063
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.313865
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.394218
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.141169
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.531682
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.376626
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.488787
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.126704
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.196660
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.328918

experiment 4
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.412400
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.392359
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.498345
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.285608
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.443783
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.573276
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.415482
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.169437
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.457341
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.274021

experiment 5
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.301097
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.476499
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.421168
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.409623
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.497942
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.228691
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.287486
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.133129
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.272133
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.255005

experiment 6
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.495741
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.400736
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.157593
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.593680
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.337498
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.306030
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.358878
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.568347
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.582303
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.423637

experiment 7
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.514467
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.589839
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.472678
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.426310
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.481449
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.390231
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.324628
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.561055
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.390384
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.181850

experiment 8
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.248204
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.344240
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.469901
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.558743
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.361243
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.504636
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.476815
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.553882
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.225728
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.269581

experiment 9
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.320078
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.546956
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.403916
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.528128
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.406267
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.128467
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.378668
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.481325
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.161904
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.598776

experiment 10
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.553973
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.534903
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.327121
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.456718
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.214826
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.279358
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.284457
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.345226
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.236317
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.542954

experiment 11
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.214781
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.224349
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.590862
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.503402
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.518229
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.259479
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.431245
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.262139
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.134515
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.202328

experiment 12
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.153510
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.250510
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.369836
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.123822
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.380772
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.291510
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.209764
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.380579
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.184019
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.259410

experiment 13
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.503208
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.286642
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.159034
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.406550
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.293871
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.191723
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.145896
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.213109
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.596015
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.238439

experiment 14
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.353788
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.281098
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.452082
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.328970
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.233736
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.538236
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.347166
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.183397
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.170831
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.578984

experiment 15
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.536407
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.352984
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.517682
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.211185
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.484782
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.435526
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.135753
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.147229
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.384406
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.381942

experiment 16
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.597940
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.284279
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.358968
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.118274
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.338589
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.157876
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.274648
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.455493
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.346061
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.113044

experiment 17
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.433174
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.333162
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.423775
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.366278
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.242899
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.280245
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.599832
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.540680
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.565207
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.501649

experiment 18
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.446131
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.202677
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.593581
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.402067
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.508286
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.428689
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.442000
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.354138
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.341126
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.323857

experiment 19
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.473672
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.593527
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.307748
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.291938
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.419109
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.510241
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.141759
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.451621
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.565893
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.134598

experiment 20
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.527547
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.346794
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.252661
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.373118
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.290419
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.553336
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.496671
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.430588
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.388998
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.244083

experiment 21
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.342127
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.552147
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.453767
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.180630
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.153875
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.473911
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.172925
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.520245
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.317885
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.435231

experiment 22
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.278767
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.500143
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.441970
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.530329
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.544188
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.413171
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.147372
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.426189
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.161624
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.421362

experiment 23
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.255837
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.573870
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.138327
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.513338
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.233406
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.260825
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.328305
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.413970
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.189882
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.464237

experiment 24
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.216823
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.101125
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.333579
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.570108
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.443623
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.171572
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.447770
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.335498
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.452179
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.321684

experiment 25
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.273970
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.389726
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.198735
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.158960
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.267819
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.557386
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.520466
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.105264
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.551396
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.484803

experiment 26
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.370120
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.319243
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.209797
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.561351
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.331936
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.371846
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.114583
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.209419
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.407242
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.308313

experiment 27
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.158507
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.229446
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.252158
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.421406
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.438935
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.371964
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.528475
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.238533
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.184465
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.512749

experiment 28
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.240390
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.100001
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.339023
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.571285
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.285388
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.370032
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.321214
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.523212
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.123564
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.101006

experiment 29
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.166213
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.350719
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.511233
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.230980
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.124835
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.371369
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.488890
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.113954
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.485351
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.593421

experiment 30
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.524444
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.357355
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.131519
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.259827
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.387487
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.313419
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.417725
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.350920
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.475946
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.553469

experiment 31
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.165800
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.167772
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.247857
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.548272
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.462179
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.321997
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.304657
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.136876
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.512646
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.276640

experiment 32
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.186118
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.395359
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.169106
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.363039
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.584643
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.486138
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.456118
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.216935
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.138019
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.357609

experiment 33
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.541680
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.376983
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.448812
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.417039
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.351359
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.105441
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.568496
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.488897
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.578623
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.153485

experiment 34
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.181108
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.274712
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.161737
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.307780
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.327793
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.490928
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.343083
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.180633
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.344323
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.292243

experiment 35
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.237749
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.497702
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.176873
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.541579
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.512963
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.459362
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.211625
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.557496
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.110410
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.375494

experiment 36
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.282200
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.512465
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.479484
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.455350
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.127244
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.135156
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.559581
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.122329
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.403447
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.162417

experiment 37
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.211008
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.290406
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.204360
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.277310
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.196053
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.317654
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.146681
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.320156
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.145876
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.288547

experiment 38
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.162840
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.176870
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.190995
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.378177
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.343234
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.334415
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.254372
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.328997
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.122436
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.578243

experiment 39
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.121270
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.372193
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.339006
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.438561
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.129455
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.518153
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.442636
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.455280
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.232319
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.164609

experiment 40
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.444395
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.406696
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.203748
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.500844
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.384950
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.267780
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.218125
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.399568
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.595191
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.516304

experiment 41
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.345097
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.584881
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.410495
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.592338
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.325982
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.235775
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.587970
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.194170
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.312064
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.263172

experiment 42
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.341265
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.116694
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.531307
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.392442
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.581850
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.203284
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.574906
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.311234
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.219158
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.388261

experiment 43
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.116301
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.370311
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.246784
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.180289
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.222599
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.258578
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.158524
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.365397
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.298222
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.470022

experiment 44
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.545940
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.528115
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.224585
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.130308
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.198353
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.345293
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.396945
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.132127
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.251997
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.374928

experiment 45
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.299788
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.203598
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.233180
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.377869
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.575526
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.171956
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.345730
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.418169
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.467293
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.426706

experiment 46
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.312230
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.101961
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.387883
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.297699
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.337369
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.554762
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.357034
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.401599
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.102797
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.219885

experiment 47
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.352525
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.186229
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.430518
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.282390
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.129548
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.484861
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.504186
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.112262
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.549056
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.212313

experiment 48
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.147520
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.287190
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.332027
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.444809
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.523892
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.466656
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.259272
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.595093
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.285059
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.442129

experiment 49
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.526848
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.282868
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.424309
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.146920
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.574916
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.229751
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.504774
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.350852
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.515451
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.159015

experiment 50
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.326933
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.172569
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.373818
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.103205
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.275746
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.558660
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.280024
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.385485
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.379229
python3 cli.py send --from 1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W --to 1CjsJ3JguwfGRAW1CKgVYor4UgcSG2XF9n --amount 1 --fee 0.539593
