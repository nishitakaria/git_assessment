def freq(text):
	str1=text.split()               #split the text by space in list str1
	str2=[]                         #declare empty list str2
	
	for i in str1:
		if i not in str2:           #put unique words in str2
			str2.append(i)
	str2.sort()                     #sort the list str2
	
	output = open("output.txt","w")
	for i in range(0, len(str2)):
		output.write(str2[i])       #write each unique word to file
		output.write(',')           #seperate words and count by ,
		count=str1.count(str2[i])   #count the frequancy of words
		count = str(count)
		output.write(count)
		output.write('\n')          #each unique word on new line
	output.close()                  #close the file
		 

def main(): 
	input = open("input.txt","r")   #Read the input from file 'input.txt'
	text = input.read()             #read the lines of input file 
	input.close()                   #close the file
	freq(text)                      #call the freq() and pass text as parameter

if __name__ == "__main__":
	main()