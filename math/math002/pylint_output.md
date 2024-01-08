(venv) fox@enine014:~/Day2/math-002-e9gsrivastava$ pylint answer.py 
************* Module answer
answer.py:1:0: C0114: Missing module docstring (missing-module-docstring)
answer.py:1:0: C0116: Missing function or method docstring (missing-function-docstring)

------------------------------------------------------------------
Your code has been rated at 8.18/10 (previous run: 7.50/10, +0.68)

(venv) fox@enine014:~/Day2/math-002-e9gsrivastava$ pylint solver.py 
************* Module solver
solver.py:18:4: R1705: Unnecessary "else" after "return", remove the "else" and de-indent the code inside it (no-else-return)
solver.py:29:4: R1705: Unnecessary "elif" after "return", remove the leading "el" from "elif" (no-else-return)

------------------------------------------------------------------
Your code has been rated at 9.20/10 (previous run: 9.20/10, +0.00)

