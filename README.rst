==========================
中文分词器集合
==========================


.. image:: https://img.shields.io/pypi/v/chinese_tokenzier_iterator.svg
        :target: https://pypi.python.org/pypi/tokenizers_collection

.. image:: https://img.shields.io/travis/howl-anderson/chinese_tokenzier_iterator.svg
        :target: https://travis-ci.org/howl-anderson/tokenizers_collection

.. image:: https://readthedocs.org/projects/chinese-tokenzier-iterator/badge/?version=latest
        :target: https://tokenizers-collection.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status




一些中文分词器的简单封装和集合


* Free software: MIT license
* Documentation: https://tokenziers-collection.readthedocs.io.


Features
--------

* TODO

使用
----
.. code-block:: python

    from tokenizers_collection.config import tokenizer_registry
    for name, tokenizer in tokenizer_registry:
        print("Tokenizer: {}".format(name))
        tokenizer('input_file.txt', 'output_file.txt')

安装
----
.. code-block:: bash

    pip install tokenizers_collection

更新许可文件与下载模型
=======================
因为其中有些模型需要更新许可文件（比如：pynlpir）或者需要下载模型文件（比如：pyltp），因此安装后需要执行特定的命令完成操作，这里已经将所有的操作封装成了一个函数，只需要执行类似如下的指令即可

.. code-block:: bash

    python -m tokenizers_collection.helper

注意：

* 如果遇到 ``Error: unable to fetch newest license.`` 那么可能是 Python 3 的 SSL 的问题，参考 `pynlpir update error <https://github.com/tsroten/pynlpir/issues/108>`_ 或者 `How to make Python use CA certificates from Mac OS TrustStore? <https://stackoverflow.com/questions/40684543/how-to-make-python-use-ca-certificates-from-mac-os-truststore>`_ 进行解决。

* 由于需要下载的模型文件较大（600+ M），所以下载时间较长，具体情况根据当时网络情况而定，如果遇到错误，尝试重新运行命令。

Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
