# parrot security 安装注意事项

## 更新

sudo apt-get update
sudo apt-get 

## Linux 命令行qq

1 安装perl  
`sudo apt-get install perl
`
2 安装包管理器cpanm 方便安装mojoqq
`sudo cpan -i App::cpanminus
`
3 安装mojoqq  
`sudo Mojo::Webqq
`
4 安装irc模块
`sudo cpanm -v Mojo::IRC::Server::Chinese
`
5 写irc启动脚本  
`touch ircqq.pl
`
用编辑器编辑脚本  
`
#!/usr/bin/env perl
use Mojo::Webqq;
my $client = Mojo::Webqq->new();
$client->load("ShowMsg");
$client->load("IRCShell"); #加载IRCShell插件
$client->run();
`
