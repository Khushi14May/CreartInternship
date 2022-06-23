#5 subjects enter from user , get the total and get the percentage.

math=int(input('Enter the marks of maths:' ))
eng=int(input('Enter the marks of english:' ))
guj=int(input('Enter the marks of gujarati:' ))
ss=int(input('Enter the marks of ss:' ))
sci=int(input('Enter the marks of science:' ))

total=math+eng+guj+ss+sci
print("total marks of subject: ",total)
percentage=int(total/5)
print("percentage is : ",percentage,'%')
