from sys import argv

script, user_name = argv
prompt = '$ '

print('Hi %s, I\'m the %s script.' %(user_name,script))
print('like to ask u a few questions.')
print('Do u like me, %s?' %(user_name))
likes = input(prompt)

print('Where do u live, %s?' %(user_name))
lives = input(prompt)

print('What kind of pc do u have? %s' %(user_name))
pc = input(prompt)

print("""Alright, so u said %s about liking me.
 U live in %s. Not sure where it is. 
 and u have a %s pc. Nice. """ %(likes, lives,pc))