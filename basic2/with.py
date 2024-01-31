#########################################
# file = open('sample.text')
# text = file.read()
# file.close

# print(text)
#########################################

with open('sample.text') as file:
    text = file.read()
    print(text)
    
##it will implicitly/automatically close the 
##file

