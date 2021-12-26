import os
import sys

# repo_path/python
tvm_path = '/Users/allen/Repos/tvm/python'
sys.path.append(tvm_path)
import tvm

print(os.getgid())
print(tvm.__file__)

x = tvm.tir.Var("x", "int32")

# set breakpoint ast here and releated c++ code
# `src/tir/ir/expr.cc`
# `tir.Add`
y = tvm.tir.Add(x, x)
print(y)
