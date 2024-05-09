"""
.. _ref_trasient_analysis:

Transient analysis
==================
**瞬态分析**

本例展示了如何使用 PyDPF-Post 对瞬态分析结果文件进行后处理。
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
# 获取 ``Solution`` 对象。此示例加载在 Ansys Mechanical 中计算的瞬态分析结果文件。

solution = post.load_solution(examples.msup_transient)
print(solution)

###############################################################################
# Get ``Result`` objects
# ----------------------

###############################################################################
# Get displacement result
# ~~~~~~~~~~~~~~~~~~~~~~~
# 获取位移 ``Result`` 对象。

disp_result = solution.displacement()
disp = disp_result.vector

###############################################################################
# Check number of fields
# ~~~~~~~~~~~~~~~~~~~~~~
# Check the number of fields.

disp.num_fields

###############################################################################
# Get data from field
# ~~~~~~~~~~~~~~~~~~~
# Get data from a field.

disp.get_data_at_field(0)

###############################################################################
# Get maximum data value over all fields
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Get the maximum data value over all fields.

disp.max_data

###############################################################################
# Get minimum data value over all fields
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Get the minimum data value over all fields.

disp.min_data

###############################################################################
# Get maximum data value over targeted field
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Get the maximum data value over a targeted field.

disp.get_max_data_at_field(0)

###############################################################################
# Get minimum data value over all fields
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Get the minimum data value over all fields.

disp.get_min_data_at_field(0)

###############################################################################
# Get stress result
# -----------------
# 获取张量的应力 ``Result`` 对象。

stress_result = solution.stress()
stress = stress_result.tensor

###############################################################################
# Check number of fields
# ~~~~~~~~~~~~~~~~~~~~~~
# Check the number of shell and solid elements in distinct fields.

stress.num_fields

###############################################################################
# Get shell field
# ~~~~~~~~~~~~~~~
# Get the shell field.

shell_field = stress[0]
shell_field.shell_layers

###############################################################################
# Get solid field
# ~~~~~~~~~~~~~~~
# Get the solid field.

solid_field = stress[0]

###############################################################################
# Plot contour
# ~~~~~~~~~~~~
# 绘制等高线。

stress.plot_contour()

###############################################################################
# Get elastic strain result
# -------------------------
# **获得弹性应变结果**

elastic_strain_result = solution.elastic_strain()
elastic_strain = elastic_strain_result.tensor
# shell and solid elements are in distinct fields.
elastic_strain.num_fields

###############################################################################
# 如果结果文件中包含，则可以使用此方法获取弹性应变结果。

print(solution.elastic_strain())
