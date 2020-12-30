## 一些约定(重要)
* 以下所有API的URL都需要加前缀: `/api`
* router: 路由器名称。物理拓扑固定只有3个路由器，因此取值范围为`A`、`B`、`C`
* interfaceType: 路由器上的接口类型。取值范围为`f`（快速以太网）和`s`（串行接口）
* interfaceId: 第几个接口。
* 举例
  * 想要表示"路由器A上的第二个以太网接口": `/A/f/1`
  * 想要表示"路由器B上的第一个串行接口": `/B/s/0`

## 展示路由表部分
### 配置单个路由器上指定接口的IP地址和子网掩码
```js
PATCH router/{router}/{interfaceType}/{interfaceId}
{
    'ipAddress': '10.0.0.0',
    'subnetMask': '255.0.0.0'
}
```
正常返回`show ip interface [接口名]`显示的信息
```js
{
    // 设置成功后的IP地址
    'ipAddress': '10.0.0.0',
    // 设置成功后的子网掩码
    'subnetMask': '255.0.0.0',
    // 快速交换是否开启 true/false
    'ifIpFastSwitching': 'true',
    // 该接口是否被启用 true/false
    'status': 'true'
}
// 404: 指定的路由器或接口不存在
// 400: 缺少参数
```

### 获取单个路由器上指定接口的配置信息
```js
GET router/{router}/{interfaceType}/{interfaceId}
```
返回`show ip interface [接口名]`显示的信息
```js
{
    'ipAddress': '10.0.0.0',
    'subnetMask': '255.0.0.0',
    'ifIpFastSwitching': 'true',
    'status': 'true'
}
// 404: 指定的路由器或接口不存在
```

### 获取单个路由器的路由表信息
获取单个路由器中的整个路由表，返回数组，数组的每一项是一条路由表条目
```js
GET router/{router}
[
    ...
    {
        // 该路由的类型[C/R]
        'type': 'C',
        // 目的地地址
        'destinationAddress': '192.168.1.0/24',
        // 下一跳地址
        'nextHopAddress': '192.168.2.1',
        // 该路由使用的接口名
        'interface': 'Serial0/0/0'
    },
    ...
]
// 404: 指定的路由器不存在
```

### 在指定路由器的指定接口上开启RIP动态路由
```js
PATCH /router/{router}
{
    // netList为子网列表, 其中的每一项是接口所属的子网号
    // 该API的意义是在指定路由器的指定子网上关闭快速交换(fast-switching)，具体请参照实验二的1.pdf中的流程
    "netList" : [
        "192.168.1.0",
        "10.0.0.0"
    ]
}
```

## 验证负载均衡部分
### 捕获经过路由器B的数据包信息
```js
GET /ippacket
```
返回数组形式的数据包信息
```
[
    {

    }
]
```

### 向单个IP地址发送ping数据包
```js
POST /ippacket
{
    'ipAddress': '10.0.0.1'
}
```