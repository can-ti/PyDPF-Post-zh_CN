"""
.. _ref_complex_results:

Complex results from a modal or harmonic analysis
-------------------------------------------------
**模态分析或谐波分析的复杂结果**

This example shows how you can access complex results from a modal or
harmonic analysis.
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

solution = post.load_solution(examples.complex_rst)
solution.has_complex_result()

###############################################################################
# Get displacement result
# ~~~~~~~~~~~~~~~~~~~~~~~
# **获取位移结果**

###############################################################################
# 获取位移 ``Result`` 对象。它包含一个实数值域和一个虚数值域。

disp_result = solution.displacement()

###############################################################################
# Check if support has complex frequencies
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Check if the support has complex frequencies.

disp_result.has_complex_frequencies()

###############################################################################
# **计算结果**
disp = disp_result.vector
disp.num_fields

###############################################################################
# Define phase
# ~~~~~~~~~~~~
# **定义相位**

###############################################################################
# 定义相位。相位值必须是浮点数。相位单位为度。

phase = 39.0
disp_at_phase = disp_result.vector_at_phase(phase)
print(f"Maximum displacement at phase {phase}:", disp_at_phase.max_data)
print(f"There are {disp_at_phase.num_fields} fields")
real_field = disp_result.vector_at_phase(0.0)
img_field = disp_result.vector_at_phase(90.0)

real_field

###############################################################################
# Get amplitude
# ~~~~~~~~~~~~~
# **获取振幅**

disp_ampl = disp_result.vector_amplitude
disp_ampl.num_fields
disp_ampl.max_data
