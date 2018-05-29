#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 角色:学校、学员、课程、讲师
# 要求:
# 1. 创建北京、上海 2 所学校
# 2. 创建linux , python , go 3个课程 ， linux\py 在北京开， go 在上海开
# 3. 课程包含，周期，价格，通过学校创建课程
# 4. 通过学校创建班级， 班级关联课程、讲师
# 5. 创建学员时，选择学校，关联班级
# 5. 创建讲师角色时要关联学校，
# 6. 提供两个角色接口
# 6.1 学员视图， 可以注册， 交学费， 选择班级，
# 6.2 讲师视图， 讲师可管理自己的班级， 上课时选择班级， 查看班级学员列表 ， 修改所管理的学员的成绩
# 6.3 管理视图，创建讲师， 创建班级，创建课程
# 7. 上面的操作产生的数据都通过pickle序列化保存到文件里

__author__ = "Alex Li"

class School(object):
    def __init__(self,name,addr):
        self.name = name
        self.addr = addr
        self.students =[]
        self.staffs =[]
    def enroll(self,stu_obj):
        print("为学员%s 办理注册手续" %stu_obj.name )
        self.students.append(stu_obj)
        print("")
        self.staffs.append(stu_obj)
        print("%s")
    def hire(self,staff_obj):
        self.staffs.append(staff_obj)
        print("雇佣新员工%s" % staff_obj.name)

class SchoolMember(object):
    def __init__(self,name,age,sex):
        self.name = name
        self.age = age
        self.sex = sex
    def tell(self):
        pass

class Teacher(SchoolMember):
    def __init__(self,name,age,sex,salary,course):
        super(Teacher,self).__init__(name,age,sex)
        self.salary = salary
        self.course = course
    def tell(self):
        print('''
        ---- info of Teacher:%s ----
        Name:%s
        Age:%s
        Sex:%s
        Salary:%s
        Course:%s
        '''%(self.name,self.name,self.age,self.sex,self.salary,self.course))

    def teach(self):
        print("%s is teaching course [%s]" %(self.name,self.course))

class Student(SchoolMember):
    def __init__(self,name,age,sex,stu_id,grade):
        super(Student,self).__init__(name,age,sex)
        self.stu_id = stu_id
        self.grade = grade
    def tell(self):
        print('''
        ---- info of Student:%s ----
        Name:%s
        Age:%s
        Sex:%s
        Stu_id:%s
        Grade:%s
        ''' % (self.name, self.name, self.age, self.sex, self.stu_id, self.grade))
    def pay_tuition(self,amount):
        print("%s has paid tution for $%s"% (self.name,amount) )


school = School("老男孩IT","沙河")
t1 = Teacher("Oldboy",56,"MF",200000,"Linux")
t2 = Teacher("Alex",22,"M",3000,"PythonDevOps")
s1 = Student("ChenRonghua",36,"MF",1001,"PythonDevOps")
s2 = Student("徐良伟",19,"M",1002,"Linux")


t1.tell()
s1.tell()
school.hire(t1)
school.enroll(s1)
school.enroll(s2)

print(school.students)
print(school.staffs)
school.staffs[0].teach()
for stu in school.students:
    stu.pay_tuition(5000)