"""
.. _ref_compute_statistics_example:

Compute minimum and maximum of a DataFrame
==========================================
**计算 DataFrame 的最小值和最大值**

在本示例中，瞬态分析位移数据用于演示如何计算给定 DataFrame 的最小值或最大值。
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
# Load the result file
# --------------------
# **将结果文件加载到允许访问结果的 ``Simulation`` 对象中。**

###############################################################################
# 必须使用结果文件的路径实例化 ``Simulation`` 对象。例如，Windows 下为 ``"C:/Users/user/my_result.rst"`` 或 Linux 下为 ``"/home/user/my_result.rst"`` 。

example_path = examples.download_crankshaft()
# 自动检测模拟类型，请使用
simulation = post.load_simulation(example_path)

# 要启用自动完成功能，请使用等效的命令：
simulation = post.StaticMechanicalSimulation(example_path)

# 打印 simulation，了解可用内容的概况
print(simulation)

###############################################################################
# Extract displacement data
# -------------------------
# **提取位移数据**

displacement = simulation.displacement(all_sets=True)
print(displacement)

###############################################################################
# Compute the maximum displacement for each component at each time-step
# ---------------------------------------------------------------------
# **计算每个分量在每个时间步长的最大位移**

# 默认的 `axis` 参数是 MeshIndex
maximum_over_mesh = displacement.max()
print(maximum_over_mesh)
# 与之等效的命令为
maximum_over_mesh = displacement.max(axis="node_ids")
print(maximum_over_mesh)

###############################################################################
# Compute the maximum displacement for each node and component across time
# ------------------------------------------------------------------------
# **计算每个节点和组件在不同时间段的最大位移**

maximum_over_time = displacement.max(axis="set_ids")
print(maximum_over_time)

###############################################################################
# Compute the maximum displacement overall
# ----------------------------------------
# **计算整体最大位移**

maximum_overall = maximum_over_time.max()
print(maximum_overall)

###############################################################################
# Compute the minimum displacement for each component at each time-step
# ---------------------------------------------------------------------
# **计算每个分量在每个时间步的最小位移**

# 默认的 `axis` 参数是 MeshIndex
minimum_over_mesh = displacement.min()
print(minimum_over_mesh)
# 与之等效的命令为
minimum_over_mesh = displacement.min(axis="node_ids")
print(minimum_over_mesh)

###############################################################################
# Compute the minimum displacement for each node and component across time
# ------------------------------------------------------------------------
# **计算每个节点和组件在不同时间段的最小位移**

minimum_over_time = displacement.min(axis="set_ids")
print(minimum_over_time)

###############################################################################
# Compute the minimum displacement overall
# ----------------------------------------
# **计算整体最小位移**

minimum_overall = minimum_over_time.min()
print(minimum_overall)
