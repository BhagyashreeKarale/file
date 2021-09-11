# Question 3
# Aapke paas ek list hai. Iss list mein har string ko 
# ek file-question3.txt naam ki file mein nayi line mein daalo. 
# Aapki list yeh rahi:
banks_list = ["Kotak\n", "HDFC\n", "RBL\n", "SBI\n", "Bank of Baroda"]#i have written \n in the list of 
f=open("file-question3.txt","w")                                      #the elements itself as i want on
for i in banks_list:                                                  #new line.also i can't put \n in 
    f.write(i)                                                        #write as it takes only one argument
f.close()


