改动server和client

pass 可删

problem 继续修改

client genesis_block还是有问题，主要在server处理数据方面

尝试解决多节点同步无效的问题

把pow.py 中的37、38行注释了，不再输出nonce

成功解决三个节点同步问题

有时候同步会卡，有时候不会
