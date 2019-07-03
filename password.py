import re
import logging

logging.basicConfig(filename='pass.log',format='%(asctime)s %(message)s',level=logging.DEBUG)   #storing the log records in a log file

def validate(s):
	flag=0
	if (len(s)<6 or len(s)>12):                                                                 #checking the password length
		logging.error("Password length should be between 6 to 12")
		flag=1
	if(re.search('[A-Z]',s) is None):                                                           #checking for uppercase letter
		logging.error("Password should have atleast one uppercase letter")
		flag=1
	if(re.search('[a-z]',s) is None):                                                           #checking for lowercase letter
		logging.error("Password should have atleast one lowercase letter")
		flag=1
	if(re.search('[0-9]',s) is None):
		logging.error("Password should have atleast one number")
		flag=1
	if(re.search('[@$#]',s) is None):                                                            #checking for special character
		logging.error("Password should have atleast one special character from $@#")
		flag=1
	if(flag==0):                                                                                 #checking if all the required conditions are satisfied
		print("Valid password")
	else:
		print("Invalid password")

def main():
	s=input("Enter the password: ")                                                               #accepting the input
	logging.info('Reading the password')	
	validate(s)

if __name__ == "__main__":
	main()
