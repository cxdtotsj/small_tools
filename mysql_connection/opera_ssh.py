# -*- coding: utf-8 -*-
# @Data : 2019-10-24


from itertools import zip_longest
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import paramiko

SERVER_SSH = {
    "ip": '192.168.220.102',
    "port": 22,
    "username": "root",
    "password": "!wget@drds!win10",
}


class SSHConnect:
    def __init__(self, server_info=None):
        """
        :params <dcit> server_info: default is SERVER_SSH
    
        """
        if server_info is None:
            server_info = SERVER_SSH
        self.host = server_info["ip"]
        self.port = server_info["port"]
        self.username = server_info["username"]
        self.password = server_info["password"]
        self._transport = self.connect()
    
    def connect(self):
        trans = paramiko.Transport((self.host, self.port))
        trans.connect(username=self.username, password=self.password)
        return trans

    def close(self):
        self._transport.close()


class SSHClient(SSHConnect):

    def __init__(self, server_info=None):
        super(SSHClient, self).__init__(server_info)
        self.client = self.client()

    def client(self):
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client._transport = self._transport
        return client

    def copy(self, src, target):
        """复制远程文件"""

        return self.cmd_string("cp {} {}".format(src, target))
        
    def remote_file_back(self, src):
        """备份远程文件"""

        bak = src + '_bak'
        return self.copy(src, bak)

    def cmd_string(self, command, **kwargs):
        """
        执行远程服务器命令, 并返回 String

        :rtype: <string>
        """
        stdout, stderr = self.cmd(command, **kwargs)
        # if stderr:
        #     raise RuntimeError(f"{command} exec failed.")
        return str(stdout.read(), encoding='utf-8'), str(stderr.read(), encoding='utf-8')

    def cmd(self, command, **kwargs):
        """执行远程服务器命令"""

        stdin, stdout, stderr = self.client.exec_command(command, **kwargs)
        return stdout, stderr
        # result = (stdout.read(), stderr.read())
        # return (str(result[0], encoding='utf-8'), str(result[1], encoding='utf-8'))

    def cmd_exit_err(self, command, **kwargs):
        """
        
        """

        stdout, stderr = self.cmd_string(command, **kwargs)
        if stderr:
            raise RuntimeError(f"{command} exec failed.")
        return stdout, stderr


    def cmd_format(self, command, callback=None):
        """
        格式化输出返回值

        :parmas <string> command: 多个命令使用 ; 隔开
        :params <fucntion> callback: 可自定义返回值的输出形式 

        """

        if not callback:
            callback = self.console
        stdout, stderr = self.cmd(command, bufsize=1)
        stdout_iter = iter(stdout.readline, '')
        stderr_iter = iter(stderr.readline, '')
        for out, err in zip_longest(stdout_iter, stderr_iter):
            if out:
                callback(out.strip())
            if err:
                callback(err.strip())
        return stdout, stderr

    @staticmethod
    def console(text):
        """
        callback 函数
        """
        print(text)

    def exit_status(self, output):
        """
        获取标准输出或标准错误的退出码, 0 表示执行成功

        params <ChannelFile> output: stdout or stderr

        
        """
        return output.channel.recv_exit_status()


class SFTPClient(SSHConnect):
    '''
    params: server_info: server 连接信息
    
    '''

    def __init__(self, server_info=None):
        super(SFTPClient, self).__init__(server_info=server_info)
        self.sftp = self.sftp_create()

    def sftp_create(self):
        sftp = paramiko.SFTPClient.from_transport(self._transport)
        return sftp

    def upload(self, local_file, remote_file):
        """上传文件至远程服务器"""

        self.sftp.put(local_file, remote_file)
    
    def download(self, remote_file, local_file):
        """从远程服务器上下载文件至本地"""

        # 判断是否存在本地重名文件
        if self.is_loacl_file(local_file):
            self.backup_local_file(local_file)
        self.sftp.get(remote_file, local_file)

    def remote_file_open(self, remote_file, mode='r', **kwargs):
        """打开远程服务器上文件"""

        return self.sftp.open(remote_file, mode, **kwargs)

    def remote_list_dir(self, remote_path):
        """获取远程服务器上指定目录下的文件列表
        
        :params remote_path: 远程服务器目录
        
        :rtype: <list>
        """

        return self.sftp.listdir(remote_path)

    def remote_mkdir(self, path, **kwargs):
        """创建远程服务器文件夹"""
        
        self.sftp.mkdir(path, **kwargs)

    def remote_file_delete(self, remote_file):
        """删除远程服务器文件"""

        self.sftp.remove(remote_file)
    
    def remote_dir_delete(self, remote_dir):
        """删除远程服务器文件夹"""

        self.sftp.rmdir(remote_dir)

    def is_remote_file(self, remote_path, remote_file):
        """检查远程文件是否在指定目录下"""        

        files = self.remote_list_dir(remote_path)
        if remote_file in files:
            return True
        else:
            return False

################### local method ###################

    def is_loacl_file(self, local_file):
        """检查本地是否存在该文件"""

        return os.path.exists(local_file)
    
    def backup_local_file(self, local_file):
        """备份本地文件"""

        bak_file = local_file + '_bak'
        # 判断是否存在 待备份文件
        if self.is_loacl_file(local_file):
            # 删除 原已备份文件
            self.delete_local_file(bak_file)
            os.rename(local_file, bak_file)
            
    def delete_local_file(self, local_file):
        """删除本地文件"""

        if self.is_loacl_file(local_file):
            os.remove(local_file)


if __name__ == "__main__":
    import time
    ssh_client = SSHClient()
    # print(ssh_client.cmd_string('mysql -ucxd -p123456 -h127.0.0.1 -P3325 -e  "show @@datasource;"'))
    stdout = ssh_client.cmd_string('mysql -ucxd -p123456 -h127.0.0.1 -P3325 -e  "show @@datasource;"')
    for i in stdout[0].split('\n'):
        print(i)


