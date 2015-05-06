from xml.dom import minidom
from Base.OperateFile import base_file
# web.xml 格式如下
# <?xml version="1.0" encoding="UTF-8" ?>
# <root>
# 	<uu value="cc">ccc-key</uu>
# 	<uu value="dd">dd-key</uu>
# </root>
def read_xml(file='D:/web.xml'):
    base_file(file).check_file()
    doc = minidom.parse(file)
    root = doc.documentElement
    postparams = root.getElementsByTagName("postparams")
    count = root.getElementsByTagName("count")
    baseurl = root.getElementsByTagName("baseurl")
    httpapi = root.getElementsByTagName("httpapi")
    method = root.getElementsByTagName("method")
    port = root.getElementsByTagName("port")
    list_xml = {}

    list_xml["count"] = count[0].getAttribute("value")
    list_xml["baseurl"] = baseurl[0].getAttribute("value")
    list_xml["httpapi"] = httpapi[0].getAttribute("value")
    list_xml["method"] = method[0].getAttribute("value")
    list_xml["postparams"] = postparams[0].getAttribute("value")
    list_xml['port'] = port[0].getAttribute("value")
    return list_xml




