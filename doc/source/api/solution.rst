.. _ref_api_solution:

*********************
``DpfSolution`` class
*********************

:class:`DpfSolution <ansys.dpf.post.dpf_solution.DpfSolution>` 类是浏览结果文件内容的入口。

这段代码展示了如何加载结果文件：

.. code:: python

    >>> from ansys.dpf import post
    >>> from ansys.dpf.post import examples
    >>> solution = post.load_solution(examples.multishells_rst)

.. autosummary::
   :toctree: _autosummary

   ansys.dpf.post.load_solution
   ansys.dpf.post.dpf_solution.DpfSolution
