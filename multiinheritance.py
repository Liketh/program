class college:
    cname="Gitam"
    cplace="Bangalore"
    def branches(self):
        print("CSE,ECE,EEE,Mech,Civil")
class student(college):
    sname="Liketh"
    sid=6060
class faculty(student):
    fname="Ranjitha Madam"
    fbranch="CSE"
s1=faculty()
print(s1.sname)
print(s1.cplace)
print(s1.fname)
# Since we are able to get the values of parent and grandparent class in the child class, multi level inheritance is successfull.