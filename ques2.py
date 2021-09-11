# Question 2
# Aapne jo pichle question mein (Question 1) file download kari hai, 
# usko read karke usme number of lines count kar ke print karein. 
# Aapne sirf uss file ki number of lines Count karne ka code likhna hai. 
# Hint: Har \n ke baad nayi line shuru hoti hai. Aap yeh use kar ke nayi line ka ko pehchan sakte ho.
fileo=open("people1-exercise.txt","r")
filer=fileo.readline()
count=1
for line in fileo:
    count=count+1
print("There are",count,"lines present in'people1-exercise.text'")
fileo.close()
#another code
fileo=open("people1-exercise.txt")
filer=fileo.readlines()
print(len(filer))