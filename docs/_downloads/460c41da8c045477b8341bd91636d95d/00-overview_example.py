"""
.. _ref_overview_example:

PyDPF-Post overview
===================
**PyDPF-Post 概述**

本例概述了如何使用 PyDPF-Post。
"""

###############################################################################
# Perform required imports
# ------------------------
# **执行所需的导入**

###############################################################################
# 本示例使用了一个提供的文件，您可以通过导入 DPF ``examples`` 包获得该文件。
from ansys.dpf import post
from ansys.dpf.post import examples

###############################################################################
# Get ``Solution`` object
# -----------------------

# 获取允许访问结果的 ``Solution`` 对象。``Solution`` 对象必须使用结果文件的路径实例化。例如，Windows 下为 ``"C:/Users/user/my_result.rst"`` 或 Linux 下为 ``"/home/user/my_result.rst"`` 。

solution = post.load_solution(examples.multishells_rst)

###############################################################################
# Get mesh and time/frequency support
# -----------------------------------
# **获得网格和时间/频率支持**

###############################################################################
# 网格是模型的支撑。
# 时间/频率支持是模型的时间/频率表示。

mesh = solution.mesh
time_freq_support = solution.time_freq_support

###############################################################################
# Get ``Result`` object
# ---------------------
# **获取 ``Result`` 对象**

###############################################################################
# 从 ``Solution`` 对象获取一个 ``Result`` 对象。 ``Result`` 对象可以是应力、塑性应变、弹性应变、温度或位移。

post.print_available_keywords()
stress = solution.stress(location=post.locations.nodal, time_scoping=[1]) # 时间范围

# 在应力结果的定义中，可以使用 ``location`` 和 ``time_scoping`` 。

stress.definition.location
stress.definition.time_scoping

print(stress)

###############################################################################
# Compute data
# ------------
# **计算数据**
#
# **SX 子结果**
#
# 该代码得到的子结果 ``SX`` 是 XX 方向的应力张量。

sx = stress.xx # 首先从 stress 对象中获取 xx 组件的应力，然后存储在 sx 中
sx.num_fields # 获取 sx 的字段数量（num_fields）
sx_field = sx[0] # 获取 sx 的第一个字段，并将其存储在 sx_field 中
sx_data = sx.get_data_at_field(0) # 调用 sx 的 ``get_data_at_field`` 方法，获取第一个字段的数据，并将其存储在 sx_data 中
print("数据长度：", len(sx_data))
print("-------------------------------")
print("最大应力场：\n", sx.max)
print("-------------------------------")
print("应力场的最大数据：", sx.max_data)
print("应力场字段 0 的最大 SX：", sx.get_max_data_at_field(0))

###############################################################################
# **应力张量结果**
#
# 该代码可获取所有方向（`XX```, `XY``, `XZ``, `XY``, `YZ`` 和 `XZ``）的场的最小和最大应力。

s = stress.tensor
s_field = s[0]
s_data = sx.get_data_at_field(0)
print("数据长度：", len(s_data))
print("-------------------------------")
print("最大应力场：\n", s.max)
print("-------------------------------")
print("应力场的最大数据：", s.max_data)
print("应力场字段 0 时的最大应力张量：\n", s.get_max_data_at_field(0))
print("===============================")
print("最小应力场：\n", s.min)
print("-------------------------------")
print("应力场的最小数据：", s.min_data)
print("应力场字段 0 处的最小应力张量：\n", s.get_min_data_at_field(0))


###############################################################################
# Plot result
# -----------
# **绘制结果**

###############################################################################
# 使用 ``plot_contour()`` 方法绘制结果。

s.plot_contour()
