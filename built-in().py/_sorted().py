####################################################

nums: list[int] = [1, 2, 5, 7, 3, 6, 4]
nums2: list[int] = [1, 2, 5, 7, 3, 6, 4]
strings: list[str] = ['A', 'b', 'C', 'd', 'e', 'F']
nums.sort()

print(nums.sort())
print(nums)

sorted_numbers: list[int] = sorted(nums)

print(sorted_numbers)

print(sorted(nums, reverse=True))

print('\n')
# .sort() it returns none
####################################################

strings: list[str] = ['A', 'b', 'C', 'd', 'e', 'F']

sorted_strings: list[int] = sorted(strings)

print(sorted_strings,'\n')
#prioritize the uppercase letter over the lowercase in the ordering

print(sorted(strings, key=str.lower))
print(sorted(strings, key=str.upper), '\n\n')
#it's going convert into to lower/uppercase 
# and then compare

####################################################

class Fruit:
    def __init__(self, name: str, calories: float):
        self.name = name
        self.calories = calories
        
    def __repr__(self):
        return f'{self.name}: {self.calories}'
    

fruits: list[Fruit] = [
    Fruit('Apple',250),
    Fruit('Bannana',150),
    Fruit('Apple',100)
]

def sort_by_names(fruit: Fruit):
    return fruit.name

def sort_by_calories(fruit: Fruit):
    return fruit.calories
    
sorted_fruits: list[Fruit] = sorted(fruits, key=sort_by_calories)

print(fruits)
print(sorted_fruits)
print(sorted(fruits, key=sort_by_names), '\n')

print(sorted(fruits, key=str))
print(sorted(fruits, key=str, reverse=True))
#compare string if they are it also consider calories too
####################################################
