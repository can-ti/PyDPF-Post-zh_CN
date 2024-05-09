"""
.. _ref_dataframe_example:

Create and manipulate a DPF Dataframe
=====================================
**创建和操作 DPF Dataframe**

在此脚本中，通过从静态模拟中提取结果来生成 DataFrame。然后，它展示了不同的 Dataframe 查看和操作可能性。
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
# Get the ``Simulation`` object
# -----------------------------
# **获取允许访问结果的 ``Simulation`` 对象**

###############################################################################
# 必须使用结果文件的路径实例化 ``Simulation`` 对象。例如，Windows 下为 ``"C:/Users/user/my_result.rst"`` 或 Linux 下为 ``"/home/user/my_result.rst"`` 。

example_path = examples.download_crankshaft() # 曲轴示例
# 自动检测模拟类型，请使用
simulation = post.load_simulation(example_path)

# 要启用自动完成功能，请使用等效的命令：
simulation = post.StaticMechanicalSimulation(example_path)

# 打印 simulation ，了解可用内容的概况
print(simulation)

###############################################################################
# Get a ``Dataframe`` object
# --------------------------
# **以 Dataframe 数据形式提取结果**

displacement_dataframe = simulation.displacement(all_sets=True)

###############################################################################
# Dataframe 以表格形式显示，行和列标签用于标识数据。

print(displacement_dataframe)

###############################################################################
# Explore ``Index`` objects
# -------------------------
# **探索 ``Index`` 对象**

###############################################################################
# 每个数据标签都由索引对象或其专门子类型之一定义。

###############################################################################
# Dataframe 的列标签在 `Dataframe.columns` 中定义。
print(displacement_dataframe.columns)

###############################################################################
# ``ResultIndex`` 索引定义了存储在 Dataframe 中的结果。
print(displacement_dataframe.columns[0])
# print(displacement_dataframe.columns.results_index)  # equivalent

###############################################################################
# 您可以检查索引的可用值
print(displacement_dataframe.columns[0].values)

###############################################################################
# ``SetIndex`` 索引定义了可用的 set ID。
# set ID 是与模拟中的每个时间步、步长和子步长或频率相关联的唯一标识符。
# 如下所示，索引有一个名称和一个给定类型的值列表。
print(displacement_dataframe.columns[1]) # columns 属性返回一个包含所有列名的 Index 对象，然后通过索引 [1] 获取第二列的列名。
print(displacement_dataframe.columns[1].values)

###############################################################################
# Dataframe 的行标签在 `Dataframe.index` 中定义。
print(displacement_dataframe.index)

###############################################################################
# ``MeshIndex`` 定义了可获得数据的网格实体。
# 它可以存储 node ID、element ID 或 face ID。
print(displacement_dataframe.index[0])
# print(displacement_dataframe.index.mesh_index)  # equivalent
###############################################################################
# 由于可能的值列表可能很长，而且查询成本很高，因此除非明确询问，否则可能无法确定可用值列表。
print(displacement_dataframe.index[0].values)
###############################################################################
# 然后会更新 ``MeshIndex`` 以显示可用实体的实际数量。
print(displacement_dataframe.index[0])
# Important: 请注意，网格实体 ID 是根据内部数据存储结构排序的，默认情况下不是按升序排列！

###############################################################################
# ``CompIndex`` 定义了可获得数据的结果组件。
print(displacement_dataframe.index[1])
print(displacement_dataframe.index[1].values)

###############################################################################
# Change the Dataframe print
# --------------------------
# **更改 Dataframe 打印结果**

###############################################################################
# 有一些选项可以配置 Dataframe 的显示方式。
# 您可以通过以下方式更改想要显示的数据行数：
displacement_dataframe.display_max_rows = 9
print(displacement_dataframe)

###############################################################################
# 或显示的数据列数：
displacement_dataframe.display_max_columns = 2
print(displacement_dataframe)
# Notice: ``...`` 符号表示 DataFrame 在该方向上被截断。

###############################################################################
# The special case of ElementalNodal results
# ------------------------------------------
# **ElementalNodal 结果的特殊情况**

###############################################################################
# 当处理位于每个单元的每个节点（又称 ElementalNodal）上的结果时，会在创建时添加一个 ``ElementNodeIndex`` 索引，以指向单元连接中的节点编号。
stress = simulation.stress()
print(stress)
print(stress.columns)
print(stress.columns[2]) # columns 属性返回一个包含所有列名的 Index 对象，然后通过索引 [2] 获取第三列的列名（即为 "node"）。 --ff

###############################################################################
# Data selection
# --------------
# **数据选择**

###############################################################################
# 要选择特定的列或行，可使用索引名称作为 ``DataFrame.select`` 方法的参数，获取值列表：

disp_X_1 = displacement_dataframe.select(
    set_ids=[1], node_ids=[4872, 9005], components=["X"]
)
print(disp_X_1)

###############################################################################
# 您还可以使用 ``Dataframe.iselect`` 使用基于零的位置沿索引进行选择：
disp_Y_9005_3 = displacement_dataframe.iselect(
    set_ids=[2], node_ids=[1], components=[1]
)
print(disp_Y_9005_3)

###############################################################################
# Extract data
# ------------
# Once the Dataframe contains the specific data you require, extract it as an array with:
print(disp_X_1.array)
# IMPORTANT: Note that for the extraction of the Dataframe's data as an array to make sense,
# you must first filter the columns label values to a unique combination of values.
# The exception is for ElementalNodal data, which is returned as a 2D array.
print(stress.array.shape)

###############################################################################
# Plot a Dataframe
# ------------------
displacement_dataframe.plot()

###############################################################################
# Animate a transient Dataframe
# -----------------------------
displacement_dataframe.animate()
