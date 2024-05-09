"""
.. _ref_modal_analysis:

Modal analysis
==============
**模态分析**

本例展示了如何使用 PyDPF-Post 对模态分析结果文件进行后处理。
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

# 此示例加载了一个在 Ansys Mechanical 中计算的模态分析结果文件。

example_path = examples.download_all_kinds_of_complexity_modal()

solution = post.load_solution(example_path)
print(solution)


###############################################################################
# Get ``Result`` objects
# ----------------------
# **获取 ``Result`` 对象**

###############################################################################
# Get displacement result
# ~~~~~~~~~~~~~~~~~~~~~~~
# **获取位移结果**

###############################################################################
# 获取位移 ``Result`` 对象。它包含一个实数值域和一个虚数值域。

disp_result = solution.displacement()
disp = disp_result.vector

###############################################################################
# Check number of fields
# ~~~~~~~~~~~~~~~~~~~~~~
# **Check the number of fields**

disp.num_fields # `num_fields` 属性通常表示数据的维度或字段的数量。

###############################################################################
# **Get data from a field**

disp.get_data_at_field(0)

###############################################################################
# Get maximum data value over all fields
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# **获取所有 fields 的最大数据值**

disp.max_data

###############################################################################
# Get minimum data value over all fields
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# **获取所有 fields 的最小数据值**

disp.min_data

###############################################################################
# Get maximum data value over targeted field
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# **获取目标 fields 的最大数据值**

disp.get_max_data_at_field(0)

###############################################################################
# Get minimum data value over all fields
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# **获取目标 fields 的最小数据值**

disp.get_min_data_at_field(0)

###############################################################################
# Get stress result
# -----------------
# **获取应力结果**

###############################################################################
# 获取处理振幅的应力结果。它包含一个实值域和一个虚值域。

stress_result = solution.stress()

###############################################################################
# Check if support has complex frequencies
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# **检查是否支持复频率**

stress_result.has_complex_frequencies()

###############################################################################
# Get tensor result
# ~~~~~~~~~~~~~~~~~
# **获取张量结果**

stress = stress_result.tensor
stress.num_fields

###############################################################################
# Get shell field
# ~~~~~~~~~~~~~~~
# **获取 shell_field 的壳层信息**

shell_field = stress[0]
shell_field.shell_layers

###############################################################################
# Get solid field
# ~~~~~~~~~~~~~~~
# Get the solid field.

solid_field = stress[1]
print(solid_field)

###############################################################################
# Plot amplitude contour
# ~~~~~~~~~~~~~~~~~~~~~~
# **绘制振幅等值线图**

amplitude = stress_result.tensor_amplitude # （ˈæmplɪˌtjuːd，振幅）
stress.plot_contour()

###############################################################################
# Get elastic strain result
# =========================
# **获得处理相位的弹性应变结果**

###############################################################################
# 它包含一个实值字段和一个虚值字段。

elastic_strain_result = solution.elastic_strain()
elastic_strain = elastic_strain_result.tensor

###############################################################################
# Check number of fields
# ~~~~~~~~~~~~~~~~~~~~~~
# 检查不同 fields 中壳单元和实体单元的数量。

elastic_strain.num_fields

###############################################################################
# 如果结果文件中包含，则可以使用此方法获取弹性应变结果。

print(solution.plastic_strain())
