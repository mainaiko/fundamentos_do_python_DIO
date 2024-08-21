"""
Metodos uteis:
A classe string em python é famosa por ser rica em métodos
e possuir uma interface muito facil de trabalhar.

Ex:
"""
curso = "pYthon"
print (curso.upper())
# "PYTHON"
print(curso.lower())
# "python"
print(curso.title())
# "Python"

curso = "   Python "
print(curso.strip())
# "Python"
print(curso.lstrip())
# "Python "
print(curso.rstrip())
# "  Python"

curso = "Python"
print(curso.center(10, "#"))
# "##Python##"
print(".".join(curso))
# "P.y.t.h.o.n"

