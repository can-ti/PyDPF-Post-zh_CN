"""
.. _ref_static_analysis:

Static analysis
===============
**静态分析**

本例展示了如何使用 PyDPF-Post 对静态分析的结果文件进行后处理。
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
# **获取 ``Solution`` 对象**

# 此示例加载了一个在 Ansys Mechanical 中计算的静态分析结果文件。

example_path = examples.download_all_kinds_of_complexity()

solution = post.load_solution(example_path)
print(solution)

###############################################################################
# Get ``Result`` objects
# ----------------------
# **获取 ``Result`` 对象**

###############################################################################
# Get displacement result
# ~~~~~~~~~~~~~~~~~~~~~~~
# **获取位移 ``Result`` 对象**

disp_result = solution.displacement()
disp = disp_result.vector
print(disp)

###############################################################################
# Check number of fields
# ~~~~~~~~~~~~~~~~~~~~~~
# Check the number of fields.

print(disp.num_fields)

###############################################################################
# Get data from field
# ~~~~~~~~~~~~~~~~~~~
# Get data from a field.

print(disp.get_data_at_field(0))

###############################################################################
# Get maximum data value over all fields
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# **获取所有 fields 的最大数据值**

print(disp.max_data)

###############################################################################
# Get minimum data value over all fields
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# **获取所有 fields 的最小数据值**

print(disp.min_data)

###############################################################################
# Get maximum data value over targeted field
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# **获取目标 fields 的最大数据值**

print(disp.get_max_data_at_field(0))

###############################################################################
# Get minimum data value over all fields
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# **获取目标 fields 的最小数据值**

print(disp.get_min_data_at_field(0))

###############################################################################
# Get stress result
# -----------------
# **获取张量的应力 ``Result`` 对象**

stress_result = solution.stress()
stress = stress_result.tensor

###############################################################################
# Check number of fields
# ~~~~~~~~~~~~~~~~~~~~~~
# 检查不同 fields 中壳单元和实体单元的数量。

print(stress.num_fields)

###############################################################################
# Get shell field
# ~~~~~~~~~~~~~~~
# Get the shell field.

shell_field = stress[0]
print(shell_field.shell_layers)

###############################################################################
# Get solid field
# ~~~~~~~~~~~~~~~
# Get the solid field.

solid_field = stress[1]

###############################################################################
# Plot contour
# ~~~~~~~~~~~~
# **绘制等值线图**

stress.plot_contour()

###############################################################################
# Get elastic strain result
# -------------------------
# **获得弹性应变结果**

elastic_strain_result = solution.elastic_strain()
elastic_strain = elastic_strain_result.tensor

###############################################################################
# Check number of fields
# ~~~~~~~~~~~~~~~~~~~~~~
# 检查不同 fields 中壳单元和实体单元的数量。
print(elastic_strain.num_fields)

###############################################################################
# 如果结果文件中包含，则可以使用此方法获取弹性应变结果。

print(solution.plastic_strain())

###############################################################################
# 您也可以使用这种方法获得温度结果。

print(solution.structural_temperature())
