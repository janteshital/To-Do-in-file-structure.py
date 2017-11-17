import time
print("***************************TO-DO APPLICATION************************")
print("Enter the operation you want to perform :")
print(" a for add task to app\n v to view tasks\n d to delete task\n r to reset app")
s=raw_input()
if s=='a':
	f=open('TO-DO.txt','a')
	print("Enter the text in 'index task' format")
	task=raw_input()
	time1='\t'+str(time.strftime("%I:%M:%S"))
	date1="\t"+str(time.strftime("%d/%m/%Y"))+"\t"
	f.write('\n'+task+time1+date1)
	f.close()
if s=='v':
	f1=open('TO-DO.txt','r')
	tsk=f1.read()
	print("*********************************************************")
	print("id+task\ttime\tdate")
	print(tsk)
	print("*********************************************************")
	f1.close()
if s=='d':
	print("enter the index whose task u want to delete")
	n=raw_input()
	with open("TO-DO.txt","r+") as f:
		new_f = f.readlines()
		f.seek(0)
		for line in new_f:
			if n not in line:
				f.write(line)
		f.truncate()
if s=='r':
	f=open('TO-DO.txt','w')
	f.close()


	
