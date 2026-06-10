class Student:
    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa

    # 1 String representation (user-friendly)
    def __str__(self):
        return f"{self.name} (GPA: {self.gpa})"

    # 2️ Official representation (debugging)
    def __repr__(self):
        return f"Student(name={self.name}, gpa={self.gpa})"

    # 3️ Equality comparison (==)
    def __eq__(self, other):
        if not isinstance(other, Student):
            return False
        return self.name == other.name and self.gpa == other.gpa

    # 4️ Length (len(obj))
    def __len__(self):
        return len(self.name)

    # 5️ Callable object (obj())
    def __call__(self):
        return f"{self.name} is callable"

    # 6️ Attribute access fallback
    def __getattr__(self, item):
        return f"Attribute '{item}' not found"

    # 7️ Add operator (+)
    def __add__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        avg_gpa = (self.gpa + other.gpa) / 2
        return Student(f"{self.name}&{other.name}", avg_gpa)


s1 = Student("Spongebob", 3.2)
s2 = Student("Patrick", 2.0)

print(s1)                 # __str__
print(repr(s1))           # __repr__

print(s1 == s2)            # __eq__
print(len(s1))             # __len__

print(s1())                # __call__

print(s1.age)              # __getattr__

s3 = s1 + s2               # __add__
print(s3)
