from django.shortcuts import render
from django.http import HttpResponse
from django.http.response import JsonResponse
import telnetUtil.test
import json
# Create your views here.

routers = {'A': '192.168.3.2', 'B': '192.168.3.1', 'C': '192.168.3.3'}
password = "CISCO"

def index(request):
    return HttpResponse("Hello, world.")

def routeTable(request, router):
    name = request.method
    ret = []
    if name == 'GET':
        #telnetUtil.test.showIpRoute("192.168.3.1",password)
        router = '192.168.3.2'
        intType = 'f0'
        intId = '/0'
        ip = '11.0.0.1'
        mask = '255.255.255.0'
        #telnetUtil.test.configInt(router, password, intType, intId, ip, mask)
        temp = {}
        temp['type'] = 'C'
        temp['destinationAddress'] = '192.168.1.0/24'
        temp['nextHopAddress'] = '192.168.2.1'
        temp['interface'] = 'Serial0/0/0'
        ret.append(temp)
        return JsonResponse(ret, safe=False, json_dumps_params={'ensure_ascii': False})
        pass
    elif name == 'PATCH':
        # RIP配置
        # router 路由器ip,password 密码, net 子网ip

        # 从请求url获取参数
        netList = json.loads(request.body)['netList']
        # router = "192.168.3.2"
        # password = "CISCO"
        # netList = "rta"

        # 调用工具类配置
        telnetUtil.test.configRIP(routers[router], password, netList)

        # 返回配置结果
        result = ''
        return JsonResponse([], safe=False, json_dumps_params={'ensure_ascii': False})



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

def set_interface(request, router, intType, intId):
    if request.method == 'PATCH':
        # router 路由器ip, password 密码, intType 接口类型, intId 接口号, ip 配置ip, mask 掩码
        # 从请求url获取参数
        s = json.loads(request.body)
        ip = s['ip']
        mask = s['mask']
        router = routers[router]

        # password = 'CISCO'
        # intType = 'f0'
        # intId = '/0'
        # ip = '11.0.0.1'
        # mask = '255.255.255.0'

        # 调用工具类设置接口参数
        if intType == 'f':
            intId = '/' + intId
        if intType == 's':
            intId = '/0' + '/' + intId
        intType = intType + '0'
        telnetUtil.test.configInt(router, password, intType, intId, ip, mask)

        ret = []
        ret.append(intId)
        ret.append(password)
        ret.append(intType)
        ret.append(mask)
        ret.append(router)
        ret.append(ip)
        return JsonResponse(ret, safe=False, json_dumps_params={'ensure_ascii': False})
