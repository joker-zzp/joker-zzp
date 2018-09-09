# parrot security 安装注意事项

### Linux 装在U盘启动事项

(initramfs)启动错误，主要原因是启动盘选择的不对

进入 initramfs 模式后输入命令：`blkid`查看磁盘号,记住磁盘号`/dev/sdc1`(每个人的都不一样）

重启系统在进入grub界面按‘e’进行编辑启动文件

将Linux=... 的磁盘号`/dev/sda1 ro` 改为当前启动磁盘号`/dev/sdc1`，讲`ro`改为`rw, ro` 按 F10 重新引导启动即可进入系统

进入系统后打开终端，更新grub.cfg文件

`sudo update-grub`

这里必须执行，这里会重新扫描启动项，生成启动引导，以uuid方式标记硬盘，所以拿到别的电脑上也不会出现启动错误。

### 更新

`sudo apt-get update`  
`sudo apt-get dist-upgrade`  

### 更改语言设定针对命令行中文方块

`dpkg-reconfigure locales`

打开图形界面，空格键选中

```
en_US.UTF-8
zh_CN.UTF-8
```

将中文设置成默认后，重启即可

### 配置SSH

编辑sshd_config文件

`sudo vim /etc/ssh/sshd_config`

将sshd_config文件中的语句

`"PermitRootLogin prohibit-password"`

修改为：

`"PermitRootLogin yes"`

保存文件,启动SSH服务

`sudo service ssh start`

设置SSH开机自启动

`sudo update-rc.d ssh enable`

### 安装常用软件

#### 安装搜狗输入法

官网下载[搜狗拼音输入法 for Linux](https://pinyin.sogou.com/linux/?r=pinyin)

`sudo dpkg -i sougoupinyinXXX.deb`

#### 安装谷歌拼音输入法

`sudo apt-get install fcitx-googlepinyin` 谷歌拼音

#### 安装Google Chrome

下载Linux版[Chrome离线包](http://www.google.cn/chrome/browser/desktop/index.html)

```
sudo dpkg -i google-chrome-stable_current_amd64.deb
sudo apt-get -f install
sudo dpkg -i google-chrome-stable_current_amd64.deb
```

### Linux 命令行qq

1.安装perl

`sudo apt-get install perl`

2.安装包管理器cpanm 方便安装mojoqq

`sudo cpan -i App::cpanminus`

3.安装mojoqq

`sudo Mojo::Webqq`

4.安装irc模块

`sudo cpanm -v Mojo::IRC::Server::Chinese`

5.写irc启动脚本

`touch ircqq.pl`

6.用编辑器编辑脚本

```
#!/usr/bin/env perl
use Mojo::Webqq;
my $client = Mojo::Webqq->new();
$client->load("ShowMsg");
$client->load("IRCShell"); #加载IRCShell插件
$client->run();
```

7.安装 weechat

`sudo apt install weechat`

8.在weechat中连接服务器

`/server add ircqq localhost`

`/connect ircqq`

