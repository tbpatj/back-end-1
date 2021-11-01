def helloWorld():
    print("Hello, World!");

def printName(name):
    print(name);

def greeting(name):
    print('Hello, ' + name);

def add(num1, num2):
    return num1 + num2;

def nameCheck(name):
    if(name == 'Steven'):
        return 'what up steven';
    elif(name == 'Bryan'):
        return 'Hey Bryan!';
    else:
        return 'Cool name, name';

def faveColorFinder(color):
    if(color == 'red'):
        return 'red is a great color';
    elif(color == 'green'):
        return 'green is a solid favorite color';
    elif(color == 'black'):
        return 'so trendy';
    else:
        return 'you need to evaluate your favorite color choice';

def printAllNames(names):
    for i in names:
        print(i);

def thatsOdd(num):
    if(num % 2 == 0):
        return "That's not odd!"
    else:
        return 'That is odd indeed!'

def bigOrSmall(nums):
    answers = [];
    for num in nums:
        if(num > 100):
            answers.append("big");
        else:
            answers.append("small");
    return answers

def theEliminator(contestants, loser):
    for person in contestants:
        if(person == loser):
            contestants.remove(loser);
    return contestants

print(nameCheck('fjasdf'));
helloWorld();
printName("george");
greeting('yeah');
colorRating = faveColorFinder('red');
print(colorRating);
printAllNames(["joe","george","jerry","tina"])
oddChecker = thatsOdd(45)
bigSmallResults = bigOrSmall([12,3,43,35,35,53,35,3423,23,5,3443,5])
newList = theEliminator(['Katniss', 'Peeta', 'Fox-face', 'Glimmer', 'Cato', 'Rue', 'Thresh', 'Clove', 'Marvel'],'Clove')
print(newList);