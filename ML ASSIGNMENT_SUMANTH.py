# Question 1
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
print("AFTER SORTING",ages)  # after sorted
print("the maximum of the index is  ", max(ages))  # maximum age
print("the minimum of the index is  ", min(ages))  # minimum age
print("On adding max and min values to index and afer sorting them")
ages.append(max(ages))  # adding maximum value to index
ages.append(min(ages))  # adding minimum value to index
ages.sort()
print(ages)
index = len(ages)//2
median=sum(sorted(ages)[index - 1:index + 1]) / 2  # median
print ("the median value", median)
avg= sum(ages)/len(ages)    # average
print("the average value is", avg)
ranges = max(ages)-min(ages)  # range
print("The range is ", ranges)
print("......................")

# Question 2
dog={}
dog['name'] = 'rocky'
dog['colour'] = 'black'
dog['breed'] = 'rottweiler'  # added items to the dog dictionary
dog['legs'] = 'normal'
dog['age'] = '1year'
student = {
    'first_name': 'SAI SUMANTH',
    'last_name': 'KOLANUAPAKA',
    'Gender': 'MALE',             # created student dictionary
    'age': 22,
    'marital status': 'single',
    'skills': ['Java', 'C', 'Python'],
    'country': 'INDIA',
    'address': 'HELLO street',
    'City': 'HYDERABAD',
}
print("the length of student dictionary", len(student))   # Get the length of the student dictionary
print("the skills of student", student.get('skills'))     # to get the value of skills
print(type(['skills']))                                     # for datatype
student['skills'].append('HTML')  # two skills added
student['skills'].append('c++')
print("ATER UPDATING skills",student)
key = student.keys()              # for keys as list
print(key)
val = student.values()           # for values as list
print(val)
print("......................")


# Question 3
# Creation of a tuple
brother=('raj', 'raghava','SAI')
sisters=('pratushya', 'Swathi')
siblings=brother+sisters           # adding and assigning brothers,sisters to siblings
print("MY SIBLINGS ARE" ,siblings)
print("the no of siblings i have are",len(siblings))  # length of tuple
familymembers = siblings+('DURGA RAO','SRIDEVI RAO')  # adding father and mother names
print("THe family members are", familymembers)
print("......................")


# Question 4
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]
print("THE LENGTH OF IT COMPANIES IS ",len(it_companies))  # length
it_companies.add('TCS')                      # adding to set it_companies
it_companies.update(['INFOSYS','COGNIZANT','WIPRO'])  # adding multiple it companies to set
print("THE IT COMPANIES ARE", it_companies)
it_companies.pop()      # remove one value from set
print("THE COMPANIES AFTER REMOVING RANDOM COMPANY",it_companies)
# The difference between remove and discard is that remove() method displays an error if the element is missing in a set , where as discard() method doesn't display anything if any element is missing
C=A.union(B)  # join a and b sets
print("A UNION B",C)
print("A INTERSECTION B",A.intersection(B))  # a intersection b
print("A SUBSET B?",A.issubset(B))  # a subset b?
print("A IS DISJOINT OF B?",A.isdisjoint(B))  # a disjoint b?
A.update(B)  # joining a with b
B.update(A)  # joining b with a
print("UPDATED A after joining with b",A)
print("UPDATED B after joining with a",B)
print("SYMMETRIC DIFFERENCE BETWEEN A AND B is :",A.symmetric_difference(B))  # symmetric difference
del A  # deleting all sets
del B
del it_companies
a=len(age)  # converting age list into set
b=set(age)
print("THE AGE AFTER CONVERTING INTO SET",b)
c=len(b)
print("the length of age is " ,a,"the length of age after becoming set is", c)
print("......................")


# Question 5
r = 30   # radius
_area_of_circle_ = 3.14*r**2
print('area of circle is ', _area_of_circle_)
_circum_of_circle = 2*3.14*r
print('circumference of circle is ',_circum_of_circle)
in_radius = int(input("Enter the radius of circle"))  # radius as an input
in_area = 3.14*in_radius**2
print('The area of circle of radius {} is {}'.format(in_radius,in_area))
print("......................")

# Question 6
string = 'I am a teacher and I love to inspire and teach people'
lis = string.split()  # using split methods
unique_words = set(lis)
print(unique_words)
print("......................")

# Question 7
# Using tab escape sequence
print("Name\t    Age\t Country\t City\nAsabeneh\t250\t Finland\t Helsinki")
print("......................")

# Question 8
# String formatting method
radius = 10
area = 3.14*radius**2  # area
print('The area of a circle with radius {0} is {1} meters square'.format(radius,int(area)))
print("......................")

# Question 9
N = int(input("enter number of students"))  # input from user
lb = []
print("enter the weights of {} students in lbs".format(N))
for i in range(N):
 lb.append(int(input()))
 kg = []
for i in range(N):
 value = "{:.2f}".format(lb[i]*0.45359237)  # converting lbs to kgs
 kg.append(float(value))
print(kg)
