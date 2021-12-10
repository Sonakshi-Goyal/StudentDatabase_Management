list1=[]
class Student:
    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno
        
    def add(self):
        list1.append(obj)
        print("Added successfully")

    def delete(self,rollno):
        flag=0
        for i in range(len(list1)):
            if(list1[i].rollno==rollno):
                del list1[i]
                print("Deleted successfully")
                flag=1
                break
        if(flag==0):
            print("Roll no does not exist")
        
    def display(self):
        print("Roll no"+"\t\t"+"Name")
        for i in range(len(list1)):
            print(list1[i].rollno+"\t\t"+list1[i].name)

    def update(self, rollno, newno,name):
        flag=0
        for i in range(len(list1)):
            if(list1[i].rollno==rollno):
                list1[i].rollno=newno
                list1[i].name=name
                print("Updated successfully")
                flag=1
                break
        if(flag==0):
            print("Roll no does not exist")

    def search(self, rollno):
        flag=0
        for i in range(len(list1)):
            if(list1[i].rollno == rollno):
                print("Roll no"+"\t\t"+"Name")
                print(list1[i].rollno+"\t\t"+list1[i].name)
                flag=1
                break
        if(flag==0):
            print("Roll no not found")
while(True):
    print("MENU")
    print("1.Add")
    print("2.Delete")
    print("3.Display")
    print("4.Update")
    print("5.Search")
    print("6.Exit")
    n=int(input("Enter your choice: "))

    if(n==1):
        name=input("Enter name of the student: ")
        rollno=input("Enter roll number of the student: ")
        obj=Student(name,rollno)
        obj.add()
        
    elif(n==2):
        rollno=input("Enter rollno to be deleted: ")
        obj.delete(rollno)
         
    elif(n==3):
        obj.display()
        
    elif(n==4):
        rollno=input("Enter the rollno to be updated: ")
        newno=input("Enter new roll number: ")
        name=input("Enter new name: ")
        obj.update(rollno,newno,name)
       
    elif(n==5):
        rollno=input("Enter roll no to be searched: ")
        obj.search(rollno)
        
    else:
        break
    
