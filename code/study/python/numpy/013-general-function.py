# 一般函数
import numpy as np

# 三角函数
x = -1

'''
np.sin(x)
np.cos(x)
np.tan(x)
np.sinh(x)
np.cosh(x)
np.tanh(x)
arccos(x)
arctan(x)
arcsin(x)
arccosh(x)
arctanh(x)
arcsinh(x)
arctan2(x,y)
arctan2(x, y) 返回 arctan(x/y)
'''

# 向量操作
'''
dot(x, y)
inner(x, y)
cross(x, y)
outer(x, y)
kron(x, y)
tensordot(x, y[, axis])
'''

# 其他操作

'''
exp(x)
log(x)
log10(x)
sqrt(x)
absolute(x)
conjugate(x)
negative(x)
ceil(x)
floor(x)
fabs(x)
hypot(x)
fmod(x)
maximum(x, y)
minimum(x, y)
'''

# 类型处理
'''
iscomplexobj
iscomplex
isrealobj
isreal
imag
real
real_if_close
isscalar
isneginf
isinf
isfinite
isnan
nan_to_num
common_type
typename
'''
# 正无穷
np.inf

# 负无穷
-np.inf

# 非法值(Not a number)
np.nan

# 检查是否为无穷
np.isinf(1.0)
np.isinf(np.inf)
# 非法值
np.array([0]) / 0
# 这并不会报错,而是返回一个非法值
# 只有0/0会得到nan, 非0值除以0会得到无穷
a = np.arange(5)
b = a / 0
print(b)

# nan与任何数比较都是False
b == np.nan

# 修改形状
'''
atleast_1d
atleast_2d
atleast_3d
expand_dims
apply_over_axes
apply_along_axis
hstack
vstack
dstack
column_stack
hsplit
vsplit
dsplit
split
squeeze
'''

# 其他有用函数
'''
fix
mod
amax
amin
ptp
sum
cumsum
prod
cumprod
diff
angle

unwrap
sort_complex
trim_zeros
fliplr
flipud
rot90
diag
eye
select
extract
insert

roots
poly
any
all
disp
unique
nansum
nanmax
nanargmax
nanargmin
nanmin

nan 开头的函数会进行相应的操作，但是忽略 nan 值

'''
