"""
.. _ref_basics:

Basic features
==============
**基本功能**

本例向您展示如何获取和使用 ``Result`` 对象。
"""

###############################################################################
# Perform required imports
# ------------------------
# **执行所需的导入**

from ansys.dpf import post
from ansys.dpf.post import examples

###############################################################################
# Get ``Solution`` object
# -----------------------
# 获取 ``Solution`` 对象，并使用结果文件的路径将其实例化。

example_path = examples.download_all_kinds_of_complexity()
solution = post.load_solution(example_path)

###############################################################################
# Get ``Result`` objects
# ----------------------

###############################################################################
# Get displacement result
# ~~~~~~~~~~~~~~~~~~~~~~~
# 获取位移 ``Result`` 对象。

displacement_result = solution.displacement()
displacement = displacement_result.vector

###############################################################################
# Get information on result
# ~~~~~~~~~~~~~~~~~~~~~~~~~
# 获取位移结果信息。

###############################################################################
# 获取 displacement 对象的 num_fields 属性，这通常表示 displacement 对象包含的字段数量。
displacement.num_fields

###############################################################################
# 调用 displacement 对象的 get_data_at_field 方法，获取第 0 个字段的数据。
disp_data = displacement.get_data_at_field(0)

###############################################################################
# 获取 disp_data 的长度，这通常表示 disp_data 包含的元素数量。
len(disp_data)

###############################################################################
# 从 disp_data 列表中获取第二个元素（在 Python 中，索引是从 0 开始的，所以索引 1 对应的是第二个元素）。
disp_data[1]

###############################################################################
# 获取 displacement 对象的 max_data 属性，这通常表示 displacement 对象包含的数据的最大值。
displacement.max_data

###############################################################################
# 调用 displacement 对象的 get_max_data_at_field 方法，获取第 0 个字段的数据的最大值。
displacement.get_max_data_at_field(0)

###############################################################################
# 获取 displacement 对象的 min_data 属性，这通常表示 displacement 对象包含的数据的最小值。
displacement.min_data

###############################################################################
# Get stress result
# ~~~~~~~~~~~~~~~~~
# **获取应力结果**

###############################################################################
# 获取张量的应力 ``result`` 对象。可以获取节点位置的结果或单元位置的结果。默认为节点位置的结果。

el_stress_result = solution.stress(location=post.locations.elemental)
nod_stress_result = solution.stress(location=post.locations.nodal)

###############################################################################
# Get information on result
# ~~~~~~~~~~~~~~~~~~~~~~~~~
# **获取有关应力结果的信息**

el_stress = el_stress_result.tensor
nod_stress = nod_stress_result.tensor

el_field = el_stress[0]
el_field.location

nod_field = nod_stress[0]
nod_field.location

el_stress.get_max_data_at_field(0)
