"""
.. _ref_get_data_from_static_simulation:

Get data from static simulation
===============================
**从静态模拟中获取数据**

本例演示了如何从先前存储的静态模拟中请求数据。可以列出可用结果，查看可以检索到哪些结果。
"""

###############################################################################
# Imports and loading simulation
# ------------------------------
# **导入和加载模拟**

from ansys.dpf import post
from ansys.dpf.post import examples

simulation = post.load_simulation(examples.static_rst)
print(simulation)

###############################################################################
# Get and plot displacements
# --------------------------
# **获取并绘制位移图**

displacement = simulation.displacement()

###############################################################################
# 打印信息
print(displacement._fc)

###############################################################################
# 绘制位移图
displacement._fc[0].plot()

###############################################################################
# Get and plot stresses
# ---------------------
# **获取并绘制应力图**

###############################################################################
# 平均各节点的 "XY" 应力分量
stress = simulation.stress_nodal(components="XY")

###############################################################################
# 打印信息
print(stress._fc)

###############################################################################
# 绘制可用应力
stress._fc[0].plot()

###############################################################################
# Get stresses at only 5 nodes
# ------------------------------
# **仅在 5 个节点位置处获取应力**

###############################################################################
# 对根据 ID 选定的前 5 个节点请求应力
stress_nodes = simulation.stress_nodal(node_ids=range(1, 6))

###############################################################################
# 打印信息
print(stress_nodes._fc)

###############################################################################
# 绘制应力图
stress_nodes._fc[0].plot()

###############################################################################
# Get stresses in a named selection
# ---------------------------------
# **获取已命名选区中的应力**

###############################################################################
# 获取模拟中第一个命名选区的名称
ns = simulation.named_selections[0]
# 请求此命名选区的节点应力
stress_named_sel = simulation.stress_nodal(named_selections=ns)

###############################################################################
# 打印信息
print(stress_named_sel._fc)

###############################################################################
# 绘制应力图
stress_named_sel._fc[0].plot()

###############################################################################
# Get stresses in a few elements
# ------------------------------
# **获取若干个单元中的应力数据**

###############################################################################
# 仅对根据 ID 选定的几个单元请求应力
stress_elements = simulation.stress_nodal(element_ids=[1, 2, 3])

###############################################################################
# 打印信息
print(stress_elements._fc)

###############################################################################
# 绘制应力图
stress_elements._fc[0].plot()

###############################################################################
# Get elemental stress and raw stresses
# -------------------------------------
# *获取单元应力和原始应力**

# 获取单元应力并打印信息
stress_elements = simulation.stress_elemental()
print(stress_elements._fc)

###############################################################################
# 请求原始应力（“ElementalNode”）并打印信息
stress_raw = simulation.stress()
print(stress_raw._fc)
