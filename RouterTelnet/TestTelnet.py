#encoding=utf-8
def do_telnet(Host, username, password, finish, commands):
    import telnetlib
    '''''Telnet远程登录：Windows客户端连接Linux服务器'''

    # 连接Telnet服务器
    tn = telnetlib.Telnet(Host, port=23, timeout=10)
    tn.set_debuglevel(2)

    # 输入登录用户名

    tn.read_until(b'ROUTER login')
    tn.write(username)

    # 输入登录密码
    tn.read_until(b'Password:')
    tn.write(password)

    # 登录完毕后执行命令

    for command in commands:
        tn.read_until(finish)
        tn.write(command)

        # 执行完毕后，终止Telnet连接（或输入exit退出）



if __name__ == '__main__':
    # 配置选项
    Host = '192.168.23.133'  # Telnet服务器IP
    username = b'root\r\n'  # 登录用户名
    password = b'\r\n'  # 登录密码
    finish = b':~# '  # 命令提示符
    commands = [b'tail -F /etc/urlog/system.log\r\n',b'ls\r\n']
do_telnet(Host, username, password, finish, commands)