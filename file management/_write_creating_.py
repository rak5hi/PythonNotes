####################################################

if 0:
    with open('sample.text', 'a') as text:
        text.write('\nNew Text')
        #added to the bottom of the file

####################################################
    
with open('sample.text', 'a+') as text:
    text.write('')
    text.seek(0)
    print(text.read())
    

""" when appending to a document, it scrolls all the way to the bottom.
    & when try to read the document,it reading wt's at bottom & that doesn't exist.
    
    seek(0):  start at position of zero once again 
    
    text.write(''): leaving it as empty string, bcz if there is some str/text
    in it, it going to append, as many times as it called
    
     a+: appending(write) and reading mode"""
####################################################
   
#with open('newfilename.text', a) as text:
#    print(text.read())
  
"""specifing a file name that doesn't exist can create a file of that name.
   OR if it exist it going to preform the operation to that specified file"""
   
####################################################

# WRITING MODE

with open('writing.text', 'w+') as text:
    text.write('REPLACING...\n')
    text.seek(0)
    print(text.read())
    
"""each time using writing mode,it replaces the entire file.
   in simple: writing mode create new file of same name of existing file
              & delete/replace the existing file"""

####################################################

# CREATING MODE
if 1:
    with open('sample.text', 'x+') as text:
        text.write('Hello world')
        text.seek(0)
        print(text.read())
                
# it throws ERROR- bcz sample.text file already exist

####################################################

# a+: appending(write) and reading mode
# w+: write mode and reading mode
# x+: creating mode and reading mode

