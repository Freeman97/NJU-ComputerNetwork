import telnetlib
import time

_UsermodTag = '>'

# 接口配置
# router 路由器ip, password 密码, intType 接口类型, intId 接口号, ip 配置ip, mask 掩码
def configInt(router, password, intType, intId, ip, mask):
    print('--start config interface--')
    # login
    tn = telnetlib.Telnet(router, port=23, timeout=10)
    tn.set_debuglevel(0)
    tn.read_until(b'Password: ')
    tn.write(password.encode('utf-8') + b'\n')
    tn.read_until(b'Router>')
    print('login success')

    # configure
    tn.write(b'enable' + b'\n')
    tn.read_until(b'Password: ')
    tn.write(b'CISCO' + b'\n')
    tn.read_until(b'Router#')
    tn.write(b'config terminal' + b'\n')
    print('config terminal')
    time.sleep(0.2)
    tn.write(b'int ' + intType.encode('utf-8') + intId.encode('utf-8') + b'\n')
    time.sleep(0.2)
    print('int ' + intType + intId)
    tn.write(b'ip address ' + ip.encode('utf-8') + b' ' + mask.encode('utf-8') + b'\n')
    print('ip address ' + ip + ' ' + mask)
    time.sleep(0.2)
    tn.write(b'no shutdown' + b'\n')
    time.sleep(0.2)
    tn.write(b'exit' + b'\n')
    time.sleep(0.2)
    tn.write(b'exit' + b'\n')
    print('---finish config interface--')
    tn.close()


# RIP配置
# router  路由器ip,password 密码, net 子网ip
def configRIP(router, password, netList):
    # login
    print('--start config network--')
    tn = telnetlib.Telnet(router, port=23, timeout=10)
    tn.set_debuglevel(0)
    tn.read_until(b'Password: ')
    tn.write(b'CISCO' + b'\n')
    tn.read_until(b'Router>')
    print('login success')

    print(router)
    # configure
    tn.write(b'enable' + b'\n')
    tn.read_until(b'Password: ')
    tn.write(password.encode('utf-8') + b'\n')
    tn.read_until(b'Router#')
    print("yes")
    tn.write(b'config terminal' + b'\n')
    print('config terminal')
    # time.sleep(1)
    tn.write(b'router rip' + b'\n')
    print('router rip')
    time.sleep(0.5)
    for net in netList:
        tn.write(b'network ' + net.encode('utf-8') + b'\n')
        print('network ' + net)
        time.sleep(0.3)
    # time.sleep(1)
    tn.write(b'exit' + b'\n')
    # time.sleep(1)
    tn.write(b'exit' + b'\n')
    print('---finish subnet config---')
    tn.close()



# 获取路由表
# router  路由器ip,password 密码
# 返回：string 路由器路由表信息
def showIpRoute(router, password):
    print('--- start: get route --- ')
    # login
    tn = telnetlib.Telnet(router, port=23, timeout=10)
    tn.set_debuglevel(0)
    tn.read_until(b'Password: ')
    tn.write(password.encode('utf-8') + b'\n')
    tn.read_until(b'Router>')
    print('login success')

    # show ip route
    tn.write(b'show ip route' + b'\n')
    response = tn.read_until(_UsermodTag.encode())
    print(response.decode())
    tn.close()
    print('--- finish: get route --- ')
    return response.decode()

def close(router, password) :
    print('--- start: close --- ')
    # login
    tn = telnetlib.Telnet(router, port=23, timeout=10)
    tn.set_debuglevel(0)
    tn.read_until(b'Password: ')
    tn.write(password.encode('utf-8') + b'\n')
    tn.read_until(b'Router>')
    print('login success')

    tn.write(b'enable' + b'\n')
    tn.read_until(b'Password: ')
    tn.write(password.encode('utf-8') + b'\n')
    tn.read_until(b'Router#')
    tn.write(b'config terminal' + b'\n')
    print('config terminal')
    time.sleep(0.2)

    tn.write(b'int f0/1' + b'\n')
    time.sleep(0.2)
    tn.write(b'no ip route-cache' + b'\n')
    tn.write(b'exit' + b'\n')

    tn.write(b'int s0/0/0'+b'\n')
    time.sleep(0.2)
    tn.write(b'no ip route-cache'+ b'\n')
    tn.write(b'exit' + b'\n')

    tn.write(b'int s0/0/1' + b'\n')
    time.sleep(0.2)
    tn.write(b'no ip route-cache' + b'\n')
    tn.write(b'exit' + b'\n')



    tn.write(b'exit' + b'\n')
    tn.close()









# debug
def debug(router, password):
    print('start config int ')
    tn = telnetlib.Telnet(router, port=23, timeout=10)
    tn.set_debuglevel(0)
    tn.read_until(b'Password: ')
    tn.write(b'CISCO' + b'\n')
    tn.read_until(b'Router>')
    print('login success')
    tn.write(b'enable' + b'\n')
    tn.read_until(b'Password: ')
    tn.write(password.encode('utf-8') + b'\n')
    tn.read_until(b'Router#')
    print("yes")
    # tn.write(b'config terminal' + b'\n')
    print('config terminal')
    time.sleep(1)
    tn.write(b'debug ip packet' + b'\n')
    time.sleep(1)
    tn.write(b'undebug all')
    response = tn.read_until(_UsermodTag.encode())
    print(response.decode())
    tn.close()


# test dynamic route
if __name__ == '__main__':
    # configInt("192.168.3.2", "CISCO", "f0", "/0", "10.0.0.1", "255.255.255.0")
    # configInt("192.168.3.2", "CISCO", "s0", "/0/0", "192.168.1.2", "255.255.255.0")
    # configInt("192.168.3.1", "CISCO", "s0", "/0/0", "192.168.1.1", "255.255.255.0")
    # configInt("192.168.3.1", "CISCO", "s0", "/0/1", "192.168.2.1", "255.255.255.0")
    # configInt("192.168.3.3", "CISCO", "f0", "/0", "10.0.0.2", "255.255.255.0")
    # configInt("192.168.3.3", "CISCO", "s0", "/0/1", "192.168.2.2", "255.255.255.0")
    # #
    # rta = [ "192.168.1.0", "10.0.0.0"]
    # rtb = [ "192.168.1.0", "192.168.2.0", "192.168.3.0"]
    # rtc = [ "192.168.2.0", "10.0.0.0" ]
    # configRIP("192.168.3.2", "CISCO", rta)
    # configRIP("192.168.3.1", "CISCO", rtb)
    # configRIP("192.168.3.3", "CISCO", rtc)
    # time.sleep(0.3)

    # showIpRoute("192.168.3.1","CISCO")

    close("192.168.3.1","CISCO")

    # debug("192.168.3.1","CISCO")
