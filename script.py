# https://www.codecademy.com/courses/learn-python-3/projects/hacking-the-fender
import csv
import json
# Q1 is importing csv Q12 we import json
# Q2
compromised_users = []
# Nothing to do with the project
##############  JUST ME STEALING THE PASSWORDS!! ####
save_passwords = [] 
##############  JUST ME STEALING THE PASSWORDS!! ####
# Q3 Q4 Q5 Q6 Q7
with open('passwords.csv') as password_file:
  password_csv = csv.DictReader(password_file)
  for row in password_csv:
    # print(row['Username'])
    compromised_users.append(row['Username'])
    # Nothing to do with the project
    ##############  JUST ME STEALING THE PASSWORDS!! ####
    save_passwords.append(row['Password'])
    ##############  JUST ME STEALING THE PASSWORDS!! ####
  
# print(compromised_users)
# Nothing to do with the project
##############  JUST ME STEALING THE PASSWORDS!! ####
# print(save_passwords, "\n")

users_passwords = [{'username': compromised_users[i], 'password': save_passwords[i]} for i in range(len(compromised_users))]
##############  JUST ME STEALING THE PASSWORDS!! ####
# Q8 Q9 Q10
with open('compromised_users.txt', 'w') as compromised_user_file:
  for user in compromised_users:
    compromised_user_file.write(user + "\n")

# Q11
# exit the with block above

# Q12
# importing json at top level

# Q13 Q14 Q15
with open('boss_message.json', 'w') as boss_message:
  boss_message_dict = {
    "recipient": "The Boss",
    "message": "Mission Success"
  }
  json.dump(boss_message_dict, boss_message, indent=2)

# Q16 Q17 Q18 Q19 basically they saying fo new_passwords.csv whats the point! we overwrite the original passwords.csv!!
with open('passwords.csv', 'w') as new_passwords_obj:
  slash_null_sig = """
 _  _     ___   __  ____                     
/ )( \   / __) /  \(_  _)                    
) \/ (  ( (_ \(  O ) )(                      
\____/   \___/ \__/ (__)                     
 _  _   __    ___  __ _  ____  ____          
/ )( \ / _\  / __)(  / )(  __)(    \         
) __ (/    \( (__  )  (  ) _)  ) D (         
\_)(_/\_/\_/ \___)(__\_)(____)(____/         
        ____  __     __   ____  _  _         
 ___   / ___)(  )   / _\ / ___)/ )( \        
(___)  \___ \/ (_/\/    \\___ \) __ (        
       (____/\____/\_/\_/(____/\_)(_/        
 __ _  _  _  __    __                        
(  ( \/ )( \(  )  (  )                       
/    /) \/ (/ (_/\/ (_/\                     
\_)__)\____/\____/\____/                     
  """
  new_passwords_obj.write(slash_null_sig)
