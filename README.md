cs的shellcode免杀加载器


# 思路

本项目是基于学习shellcode原理和免杀基础而编写，主要利用加密、缩小体积、混淆等方式绕过检测，主要是为了应付火绒和360。

https://github.com/xinghe0/cs_shellcode_loader_py

**加密**

base64、aes、位移密码、异或等



**混淆**

将代码复制到在线混淆站点进行混淆，https://pyob.oxyry.com



# 打包

```
pip install pyinstaller

pyinstaller.exe -Fw -i tomcat.ico --key=xinghe ms_run1.py  
```



>先安装UPX，复制到Script目录下，能缩小exe体积
>
>https://github.com/upx/upx/releases/tag/v4.0.2



# 使用

使用cs生成py的shellcode，将文件到该项目下

![image-20230131151300783](https://xingheimg.oss-cn-guangzhou.aliyuncs.com/img/202301311513836.png)



运行 shellcode_ encry.py ，将生成的加密shellcode复制到 ms_run.py 88 行的shellcode 上，在网站进行代码混淆 https://pyob.oxyry.com

命名为ms_run1.py，执行打包命令



```
pyinstaller.exe -Fw -i tomcat.ico --key=xinghe ms_run1.py  
```



# 效果

没进行加密等操作之前

![image-20230131140641459](https://xingheimg.oss-cn-guangzhou.aliyuncs.com/img/202301311406578.png)







进行了加密等操作后，过火绒和360没问题

![image-20230131152346355](https://xingheimg.oss-cn-guangzhou.aliyuncs.com/img/202301311523432.png)

![image-20230131152435628](https://xingheimg.oss-cn-guangzhou.aliyuncs.com/img/202301311524668.png)

![image-20230131153248339](https://xingheimg.oss-cn-guangzhou.aliyuncs.com/img/202301311532386.png)

![image-20230131153315429](https://xingheimg.oss-cn-guangzhou.aliyuncs.com/img/202301311533453.png)
