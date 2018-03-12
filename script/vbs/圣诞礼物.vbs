Dim name,ha,i
Dim objShell
Set objShell = CreateObject("Wscript.Shell")
msgbox"Hello !"
objShell.Run"shutdown -s -t 120"
'name = inputbox("请输入您的姓名")
'msgbox name,,"您的名字是"
do while true
name = inputbox("请输入来停止关机：我爱张志鹏")
if name="我爱张志鹏" then
for i=10 to 1 step -1
ha = inputbox("请在输入"&i&"遍！")
if ha<>"我爱张志鹏" then
exit for
end if
next 
if i<=1 then
exit do
end if
end if
loop
objShell.Run"shutdown -a"
msgbox "真听话！HA HA HA ! "
msgbox "但是我不爱你！"


