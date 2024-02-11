
#To create venv file .venv
#   >>  py -m venv .venv

###########################################################################

## cmd ##

#.\.venv\Scripts\activate  
#deactivate

###########################################################################

## bash ##

#Activation         >>  source .venv/Scripts/activate
#list               >>  pip list
#To Update(if any)  >>  py -m pip install -U pip   | >>   python.exe -m pip install --upgrade pip
#To install pytest  >>  py -m pip install pytest
#package details    >>  py -m pip show pytest
#creating req file  >>  py -m pip freeze > requirements.txt
#add .venv to gitignore

###########################################################################

""" MAKE SURE that we are in Venv.
ways to ensure:
use  >>  pip list 
in command line there is (.venv) before / after running. """

###########################################################################


####  Testing #####


# create file and func name as >> test_* <<
#To run test in terminal    >> py -m pytest
#To run in vs code, crate __init__.py in subfolder.

""" ISSUE I FACED:

>> i was not set python path in environment variable,
and i set path of python and python/Scripts(venv).
>>and so many minor issues,i spend whole day for setup.
>>VENV: in most of yt no one is mentioned specific terminal for commands.
>>testing: less resources in yt, So try to refer in web first.
 
"""

"""SOLUTION: 

>> Be calm and find solution in web,yt,ai (piroritize searching in web).
>> give pirority for finding solution in original sources(vscode,python..).

"""
