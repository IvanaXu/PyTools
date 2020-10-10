# -*-coding:utf-8-*-
# @auth ivan
# @time 20190128 15:44
# @goal run 014.Test_CardBinCheck
import requests
sess = requests.session()
url = "https://ccdcapi.alipay.com/validateAndCacheCardInfo.json?_input_charset=utf-8&cardNo=X-X&cardBinCheck=true"

p = sess.get(url.replace("X-X", "6250505005050505"))
print(p.content)
b'{"cardType":"CC","bank":"GCB","key":"1544449879161-9023-11.145.199.41-706583656","messages":[],"validated":true,"stat":"ok"}'

p = sess.get(url.replace("X-X", "1500676767676767"))
print(p.content)
b'{"messages":[{"errorCodes":"CARD_BIN_NOT_MATCH","name":"cardNo"}],"validated":false,"stat":"ok","key":"1500676767676767"}'
