class company:
    emp1_name="Liketh"
    emp1_id=6060
    emp2_name="xyz"
    emp2_id=7060
    emp3_name="Abc"
    emp3_id=8060
    emp4_name="def"
    emp4_id=9060
    def read(self):
        print("Details of all the employees are: ")
    def notice(self):
        print("No more employees in your company ")
s1=company()
s1.read()
print("Employee 1\nName: ",s1.emp1_name,"\nId-",s1.emp1_id)
print("Employee 2\nName: ",s1.emp2_name,"\nId-",s1.emp2_id)
print("Employee 3\nName: ",s1.emp3_name,"\nId-",s1.emp3_id)
print("Employee 4\nName: ",s1.emp4_name,"\nId-",s1.emp4_id)
s1.notice()
