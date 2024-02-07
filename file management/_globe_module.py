"""
#import glob

#if __name__ == '__main__':
    # ? matches any single character
    print(glob.glob('??dex.js'))
    #search in current folder
    
    # * matches everything
    print(glob.glob('*.js'))
    
    # [] matches any character in the sequence
    print(glob.glob('[il][n]*.js'))
    # first letter i or l & second letter should be n
    
    # [!] matches any character not in the sequence
    print(glob.glob('[!il]*.js'))
    # first letter should not be i or l
    
    # to search file in entire sysytem
    print(glob.glob('**/*.js',                     #  **/ -path + *.js
                    root_dir='/path/path../.py',
                    recursive=True,                #for continuosly look into folder
                    include_hidden=True))          # python 3.11
    #load all that at once
    
    
    globs = glob.iglob('**/*.js',                  #i - iterator
                    root_dir='/path/path../.py',
                    recursive=True,
                    include_hidden=True)
    
    print(globs.__next())
    print(globs.__next())
    ...
    
    for i, file in enumerate(globs):
        print(i, file, sep=':')
    # load one by one
        
"""

# Globe module finds all the path names matching a specified pattern
# according to the rules used by the Unix shell(unix path expansion rules), 
# although the results are returned in a arbitary order.

# HELP with looking insidenfolders and finding path names

