#Dictionaries -contain list of keywords and it is mutable datatype
a={
    'name':'Rasamsetty',
    'age':20,
    'city':'Delhi',
    'country':'India',
    'job':'Data Scientist',
    'skills':'Python,R,SQL,Java,C++'
}
a['birthday']='21-10-23'
print(a)
print(a.get('sex')) #get output for even non existed keywords as'NONE' but not error
print(a.get('sex','Male'))
print(a)

#phone number to words
phone_number={
    '1':'One',
    '2':'Two',
    '3':'Three',
    '4':'Four',
    '5':'Five',
    '6':'Six',
    '7':'Seven',
    '8':'Eight',
    '9':'Nine'
}
no=int(input("Enter the number: "))
output=''
for i in str(no):
    output+=phone_number.get(i,'!') + " "
print(output)

#Emoji Python Prog
a=input('>')
msg=a.split(' ')
Emoji={
    ':)': '😄',
    ':(': '😟'
}
output=''
for word in msg:
    output+=Emoji.get(word, word) + " "
print(output)
