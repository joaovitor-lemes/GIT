import os

print(os.name)

import sys

print(sys.platform)
print(sys.path)

from senha import gerar_senha

gerar_senha()

print(__name__)