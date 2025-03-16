import os
import sys
sys.path.insert(0, os.path.abspath('../../'))  # Додаємо шлях до проєкту

extensions = [
    'sphinx.ext.autodoc',          # Автоматичне генерування документації з docstrings
    'sphinx.ext.napoleon',         # Підтримка Google та NumPy стилю
    'sphinx.ext.viewcode',         # Додає посилання на вихідний код
    'sphinx_autodoc_typehints'     # Додає анотації типів у документацію
]

