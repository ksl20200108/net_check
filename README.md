过滤掉空信息，只加一个str在行78
握手成功，然而行80 json.loads失败
于是加入一行输出，查看当前数据
2020-07-07 16:13:26,313 - kademlia - INFO - -----in try json loads these data: b'{"code": 1, "data": {"last_height": -1, "genesis_block": ""}}'

发现原来是MSG的object里面没有serialize和deserialize的函数
添加并取代json.loads
并用eval函数将decode得到的字符串转成字典

把shake_loop沉睡的时间改为10

nonce = ""