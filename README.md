此脚本是接口压力测试的脚本,
1.web.xml是配置文件，放到d盘根目录，结果自动生成到d盘result.xls文件中
<?xml version="1.0" encoding="UTF-8" ?>
<root>
    <postparams value="{'a':'b'}">post参数</postparams>
    <count value="10"></count><!--请求总数 -->
    <baseurl value="119.XXX"></baseurl>
    <httpapi value="/qixun/index.php/QiXunManager/Interface/UserLogin?userName=ywy002&amp;password=123456&amp;token=abc123">aa</httpapi>
    <method value="GET"></method>
    <port value="0">主机接口没有默认为0</port>
 </root>
