.. _ref_api_result_data:

********************
``ResultData`` class
********************

使用 :class:`Result <ansys.dpf.core.results.Result>` 类创建 :class:`ResultData <ansys.dpf.post.result_data.ResultData>` 类。 ``Result`` 类提供了对包含在 ``Result`` 对象中的结果值的访问。

本例展示了如何访问 ``displacement`` 的结果值：
    
.. code:: python

    >>> from ansys.dpf import post
    >>> from ansys.dpf.post import examples
    >>> solution = post.load_solution(examples.multishells_rst)
    >>> displacement = solution.displacement()
    >>> result = displacement.vector

    # Access the data

    >>> result.get_data_at_field(0)
    DPFArray([[ 2.24894986e-04, -8.06099872e-05, -1.17079164e-04],
              [ 3.15660284e-04, -3.30937021e-05, -1.18384868e-04],
              [ 1.03798114e-04, -4.58764713e-05, -4.35029024e-05],
              ...,
              [-5.61467818e-04, -5.27197644e-04, -1.83607162e-04],
              [-1.09869605e-03, -1.22675467e-03, -5.62025059e-04],
              [-6.45438681e-04, -9.78889231e-04, -1.37273202e-04]])

.. autosummary::
   :toctree: _autosummary

   ansys.dpf.post.result_data.ResultData
