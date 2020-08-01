FROM daocloud.io/library/python:3.6.3-stretch

ADD . /run/
WORKDIR /run

RUN pip install -i https://pypi.tuna.tsinghua.edu.cn/simple -r requestments.txt



CMD ["python3", "cli.py", "start"]