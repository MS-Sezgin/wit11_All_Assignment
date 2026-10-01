# Soru 2: Python'da bir "School" (Okul) sınıfı oluşturun. Bu sınıf aşağıdaki özelliklere ve işlevlere sahip olmalıdır:

# Özellikler:

# "name" (isim)
# "foundation_year" (kuruluş yılı)
# "students" (öğrenciler)
# "teachers" (öğretmenler)

# Metotlar:

# add_new_student(self, student_name, class): Okula yeni bir öğrenci eklemek için kullanılan metot. Öğrencinin adını ve sınıfını alır ve "students" listesine ekler.
# add_new_teacher(self, teacher_name, branch): Okula yeni bir öğretmen eklemek için kullanılan metot. Öğretmenin adını ve branşını alır ve "teachers" sözlüğüne (dictionary) ekler.
# view_student_list(self): Okulda kayıtlı öğrencilerin listesini görüntülemek için kullanılan metot. Öğrenci adlarını ve sınıflarını listeler.
# view_teacher_list(self): Okulda görev yapan öğretmenlerin listesini görüntülemek için kullanılan metot. Öğretmen adlarını ve branşlarını listeler.

class School:
    def __init__(self,name,foundation_year,students,teachers) :
        self.name=name
        self.foundation_year=foundation_year
        self.students=students
        self.teachers=teachers

    def add_new_student(self, student_name, student_class):
        self.students.append({"student_name":student_name,"student_class":student_class})
    def add_new_teacher(self, teacher_name, teacher_branch):
        self.teachers.append({"teacher_name":teacher_name,"teacher_branch":teacher_branch})
    def view_student_list(self):
        for i in self.students:
            print(f"""{i["student_name"]}  {i["student_class"]}""")
    def view_teacher_list(self):
        for i in self.teachers:
            print(f"""{i["teacher_name"]}  {i["teacher_branch"]}""")

s=School("aaa","aaa",[],[])
s.add_new_student("ali",2)
s.add_new_student("veli",1)
s.add_new_teacher("yahya","mat")
s.add_new_teacher("said","pc")
s.view_student_list()
s.view_teacher_list()