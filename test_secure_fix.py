# -*- coding: UTF-8 -*-
try:
    from uitrace.api import *
except:
    print("cannot import module uitrace.api")

import pytest

init_driver(workspace=os.path.dirname(__file__))

def test_fix_quick():
    start_app("com.tencent.qqpimsecure")
    click('//android.widget.RelativeLayout[@resource-id="com.tencent.qqpimsecure:id/aj"]/android.widget.Button[@text="马上体验" and @resource-id="com.tencent.qqpimsecure:id/k"]', by=DriverType.UI, timeout=20)
    click('//android.widget.LinearLayout[@resource-id="com.tencent.qqpimsecure:id/do"]/android.widget.RelativeLayout[@resource-id="com.tencent.qqpimsecure:id/dr"]', by=DriverType.UI, timeout=20)
    click('//android.widget.LinearLayout[2]/android.widget.RelativeLayout/android.widget.TextView[@text="去授权"]', by=DriverType.UI, timeout=20)

    double_click("obj_1655384150387.jpg", by=DriverType.CV, timeout=30)
    double_click("obj_1655384150387.jpg", by=DriverType.CV, timeout=30)


    img = get_img()
    res =  get_text(img, text_type='ch')

    print(" text: ", res)

    click('//android.widget.RelativeLayout[1]/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.TextView[@text="立即修复"]', by=DriverType.UI, timeout=20)
    click('//android.widget.RelativeLayout[3]/android.widget.RelativeLayout', by=DriverType.UI, timeout=20)

    img = get_img()
    res =  get_text(img, text_type='ch')

    print(" text: ", res)
    stop_app("com.tencent.qqpimsecure")
