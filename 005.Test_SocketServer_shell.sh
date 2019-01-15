#!/usr/bin/env bash
# HOW TO BUILD THE SERVER.

# (1) 安装依赖组件;
yum -y install gcc gcc-c++ automake make pam-devel openldap-devel cyrus-sasl-devel openssl openssl-devel

# (2) 下载SS5;
wget "https://jaist.dl.sourceforge.net/project/ss5/ss5/3.8.9-8/ss5-3.8.9-8.tar.gz"
tar zxvf ./ss5-3.8.9-8.tar.gz
cd ss5-3.8.9
./configure
make
make install

# (3) SS5自启动;
chmod +x /etc/init.d/ss5
chkconfig --add ss5
chkconfig --level 345 ss5 on

# (4) 用户名密码验证机制;
vi /etc/opt/ss5/ss5.conf
# 修改auth和permit;
auth 0.0.0.0/0 - u
permit u 0.0.0.0/0 - 0.0.0.0/0 - - - - -

# (6) 设置用户名和密码;
vi /etc/opt/ss5/ss5.passwd
# user user

# (7) 设置端口
vi /etc/sysconfig/ss5
# SS5_OPTS=" -u root -b 0.0.0.0:8080"

# (8) 启动
service ss5 start


# IF_ERROR
/etc/init.d/network restart
# 发现报错信息：
# /etc/sysconfig/network: No such file or directory
vi /etc/sysconfig/network
# NETWORKING=yes
# NETWORKING_IPV6=no
# HOSTNAME=
# GATEWAY=192.168.0.1

