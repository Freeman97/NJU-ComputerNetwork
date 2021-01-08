from django.shortcuts import render
from django.http import HttpResponse
from django.http.response import JsonResponse
import telnetUtil.test
import json
import re
# Create your views here.

routers = {'A': '192.168.3.2', 'B': '192.168.3.1', 'C': '192.168.3.3'}
password = "CISCO"

def index(request):
    return HttpResponse("Hello, world.")

def routeTable(request, router):
    name = request.method
    if name == 'GET':
        ret = telnetUtil.test.showIpRoute(routers[router], password)
        return JsonResponse(ret, safe=False, json_dumps_params={'ensure_ascii': False})
        pass
    elif name == 'PATCH':
        # RIP配置
        # router 路由器ip,password 密码, net 子网ip

        # 从请求url获取参数
        netList = json.loads(request.body)['netList']
        print(netList)
        # 调用工具类配置
        telnetUtil.test.configRIP(routers[router], password, netList)

        # 返回配置结果
        ret = telnetUtil.test.showIpRoute(routers[router], password)
        return JsonResponse(ret, safe=False, json_dumps_params={'ensure_ascii': False})
    elif name == 'OPTIONS':
        return HttpResponse({})



# --- start: get route --- 
# login success
# show ip route
# Codes: C - connected, S - static, R - RIP, M - mobile, B - BGP
#        D - EIGRP, EX - EIGRP external, O - OSPF, IA - OSPF inter area
#        N1 - OSPF NSSA external type 1, N2 - OSPF NSSA external type 2
#        E1 - OSPF external type 1, E2 - OSPF external type 2
#        i - IS-IS, su - IS-IS summary, L1 - IS-IS level-1, L2 - IS-IS level-2
#        ia - IS-IS inter area, * - candidate default, U - per-user static route
#        o - ODR, P - periodic downloaded static route

# Gateway of last resort is not set

# R    11.0.0.0/8 [120/1] via 192.168.2.2, 00:00:19, Serial0/0/1
#                 [120/1] via 192.168.1.2, 00:00:10, Serial0/0/0
# C    192.168.1.0/24 is directly connected, Serial0/0/0
# C    192.168.2.0/24 is directly connected, Serial0/0/1
# C    192.168.3.0/24 is directly connected, FastEthernet0/1
# Router>
# --- finish: get route ---

def get_interfaces(request, router):
    if request.method == 'GET':
        router = routers[router]
        arr = []
        ret = []
        ints = ['f0/0', 'f0/1', 's0/0/0', 's0/0/1']
        arr.append(telnetUtil.test.showInterface(router, password, 'f0', '/0'))
        arr.append(telnetUtil.test.showInterface(router, password, 'f0', '/1'))
        arr.append(telnetUtil.test.showInterface(router, password, 's0', '/0/0'))
        arr.append(telnetUtil.test.showInterface(router, password, 's0', '/0/1'))
        # regular expression pattern search
        i = 0
        for text in arr:
            temp = {}
            ip_and_mask = match_ip_address(text)
            temp['interface'] = ints[i]
            i += 1
            if ip_and_mask != None:
                temp['ipAddress'] = ip_and_mask[0]
                temp['subnetInt'] = ip_and_mask[1]
                full_mask = telnetUtil.test.getIntIpMask(text)[1]
                temp['subnetMask'] = full_mask
            temp['status'] = telnetUtil.test.isUp(text)
            ret.append(temp)
        return JsonResponse(ret, safe=False, json_dumps_params={'ensure_ascii': False})

def match_ip_address(ipstr):
    # 返回匹配出的ip地址和子网掩码
    ip_pattern = re.compile(r'((2(5[0-5]|[0-4]\d))|[0-1]?\d{1,2})(\.((2(5[0-5]|[0-4]\d))|[0-1]?\d{1,2})){3}/[0-9]{1,2}')
    ip_str = ip_pattern.search(ipstr)
    if ip_str == None:
        return None
    split_ip_str = ip_str.group().split('/')
    return split_ip_str[0], split_ip_str[1]


def set_interface(request, router, intType, intId):
    router = routers[router]
    if intType == 'f':
        intId = '/' + intId
    if intType == 's':
        intId = '/0' + '/' + intId
    intType = intType + '0'
    ret = {}
    if request.method == 'PATCH':
        # router 路由器ip, password 密码, intType 接口类型, intId 接口号, ip 配置ip, mask 掩码
        # 从请求url获取参数
        s = json.loads(request.body)
        ip = s['ipAddress']
        mask = s['subnetMask']

        # password = 'CISCO'
        # intType = 'f0'
        # intId = '/0'
        # ip = '11.0.0.1'
        # mask = '255.255.255.0'

        # 调用工具类设置接口参数
        telnetUtil.test.configInt(router, password, intType, intId, ip, mask)
        temp = telnetUtil.test.showInterface(router, password, intType, intId)
        ip_and_mask = match_ip_address(temp)
        full_mask = telnetUtil.test.getIntIpMask(temp)[1]
        ret['ipAddress'] = ip_and_mask[0]
        ret['subnetMask'] = full_mask
        ret['subnetInt'] = ip_and_mask[1]
        ret['status'] = telnetUtil.test.isUp(temp)
        return JsonResponse(ret, safe=False, json_dumps_params={'ensure_ascii': False})
    elif request.method == 'GET':
        temp = telnetUtil.test.showInterface(router, password, intType, intId)
        ip_and_mask = match_ip_address(temp)
        full_mask = telnetUtil.test.getIntIpMask(temp)[1]
        ret['ipAddress'] = ip_and_mask[0]
        ret['subnetMask'] = full_mask
        ret['subnetInt'] = ip_and_mask[1]
        ret['status'] = telnetUtil.test.isUp(temp)
        return JsonResponse(ret, safe=False, json_dumps_params={'ensure_ascii': False})
    elif request.method == 'OPTIONS':
        return HttpResponse({})
