#use . format 
#a = int(input("Enter your age"))
#b = a + 1
#print("now you are {} year old and after one year you {} your age".format(b, a))
#make to ruselt 
sub1 = "Bangla"
sub2 = "English"
sub3 = "Mathematics"
ban = int(input("Enter marks in {} :".format(sub1)))
eng = int(input("Enter marks in {} :".format(sub2)))
math = int(input("Enter marks in {} :".format(sub3)))

def check_marks(sub, marks):
    if marks < 0:
        print("{}\tInvalid".format(sub))
    elif marks < 33:
        print("{}\t F".format(sub))
    elif marks < 40:
        print("{}\t D".format(sub))
    elif marks < 50:
        print("{}\t C".format(sub))
    elif marks < 60:
        print("{}\t B".format(sub))
    elif marks < 70:
        print("{}\t A-".format(sub))
    elif marks < 80:
        print("{}\t A".format(sub))
    elif marks <= 100:
        print("{}\t A+".format(sub))
    else:
        print("{}\tInvalid".format(sub))
check_marks(sub1, ban)
check_marks(sub2, eng)
check_marks(sub3, math)
