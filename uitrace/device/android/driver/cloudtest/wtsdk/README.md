[TOC]

## get code

git clone --recursive http://git.code.oa.com/cloud-open-libs/wt-open-component.git

## run demo

open demo dir

1. connect usb cable with your phone to PC
2. install apk/MultitouchTest_53.apk and run it in the phone
3. run demo.py

It is still demo code for using protobuf to communicate with touchserver/cloudscreen.
It can't be intergated in AI, cause PlatformProxy is not satisfied AI's requirements.

## overview

```
                                             +----------------+
+----------------+      HEARTBEAT_REQ        |                |
|                +-------------------------> |                |
|   mediacentre/ |      HEARTBEAT_RES        |  cloudscreen   |
|   python sdk   +<------------------------+ |                |
|                |                           |                |
|                |                           |                |
|                |   CAPTURE_PUSH_MODE_REQ   |                |
|                +-------------------------->+                |
|                |                           |                |
|                |   CAPTRUE_FRAME_NOTIFY    |                |
|                +<--------------------------+                |
|                |                           |                |
|                |                           |                |
|                |                           |                |
+----------------+                           |                |
       pc                                    +----------------+
                                                   phone
```

**心跳**

心跳包。由client发起，cloudscreen收到会回对应RES包。cloudscreen不会主动发HEARTBEAT_REQ包。这是用来探测client与cloudscreen之间的tcp链路是活的。

**截图**

截图是由手机主动推给client，也就是所谓的PUSH模式。
截图之前，client发`CAPTURE_PUSH_MODE_REQ`包，在该包中设置截图分辨率、质量、截图帧率，所以该包是用来初始化截图参数的。
如果一切正常运行，clouddscreen组件检测到手机画面有变化时，自动以设定的帧率，向client侧推送图片。也就是SCREEN_CAPTURE_FRAME_NOTIFY包。

另外，截图协议还包括获取设备显示信息的包。

`DISPLAY_DEVICE_INFO_REQ`与`DISPLAY_DEVICE_INFO_RES`。

**触摸**

触摸更简单，触摸由client侧向touchserver注入触摸点信息，不再赘述

## requirments

```
$ pip3 install -i https://mirrors.tencent.com/pypi/simple/ protobuf3
$ pip3 install -i https://mirrors.tencent.com/pypi/simple/ opencv-python
````
