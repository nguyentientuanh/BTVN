languages = ("PHP", "Python", "C#")

(php, python, c_sharp) = languages
print(php)
print(python)
print(c_sharp)

languages = ("PHP", "Python", "C#", "Java", "Visual Basic")

(php, python, *other) = languages
print(php)
print(python)
print(other)

languages = ("PHP", "Python", "C#", "Java", "Visual Basic", "Python")

# Số lần phần tử Python xuất hiện trong tuple
p = languages.count("Python")
print("Số lần phần tử Python trong tuple = ", p)

# Tìm kiếm phần tử C# trong tuple
i_c_sharp = languages.index("C#")
print("Index of C# = ", i_c_sharp)

# Nếu phần tử không tồn tại trong tuple, sẽ phát sinh lỗi
print("Index of Swift = ", languages.index("Swift"))


