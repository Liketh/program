class college:
    cname="Gitam"
    cplace="Bangalore"
    def branches(self):
        print("CSE,ECE,EEE,Mech,Civil")
class student(college):
    sname="Liketh"
    sid=6060
s1=student()
print(s1.cname)
print(s1.cplace)