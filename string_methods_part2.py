# print("hello".zfill(8)) #000hello. it fill the missing charaters with zeros . from left side.
# print("hello".zfill(3)) #if we give less number it shows the same how many charaters are there it will show that much.

# print("hello sir".center(13,"$")) #$$hello sir$$. this is use to fill the special charaters or by default it takes spaces.
# print("hellosir".center(15,"%")) #%%%%hellosir%%%

# v="  "
# u=" "
# w=""
# x="   jjcl bb"
# print(v.isspace()) #true. isspace is gives true when it has single space or multiple space.
# print(u.isspace()) #true. it is true coz it has single space
# print(w.isspace()) #False. isspace is gives False when it has empty string and some thing written in the string.
# print(x.isspace()) #False. it gives false coz something is written in string so it gives False.
# print("".isspace()) #False
# print(" ".isspace()) #True

# print("hello rohan".index("l")) #2. this is used to check where the variable is lying. the index always starts from the "0,1,2,3,...".
# print("hello challo".index("o",6)) #11. if we have multiple letters then this way is used.
# print("one plus".index("p")) #4
# print("khello jahello hello".index("e",3)) #10
# print("khello jahello hello".index("e",11)) #16

# print("hello pythoonhy".rindex("o")) #11. the rindex which means right side index it counts form right side of the variable.
# print("hello python".index("c")) #valueError:sub string is not found. if their is no varable is not mentioned in that then we will get value error.

# print("print python programming") #this rfind method where if their are more letters then find find length of it and then find rfind
# print(len("print python programming")) #24. coz the length starts form (1,2,3,4....)
# print("print python programming".rfind("m")) #20 . co the find starts from (0,1,2,3,4....)

# print("python programming".count("p"))#2. this count is used to check how many the letter is repeating.
# print("python programming".count("b")) #0. if the letter is not there in that string then we are trying to find it then it shows "0(zero)"

# print("rohan".replace("rohan","mohan")) #mohan. this replace method is used to repalce one string to another string.
# v="ravula rohan kumar"
# print(v.replace("rohan","jhon")) #ravula jhon kumar.
# x="python is good language python is useful"
# print(x.replace("python",str(5))) #5 is good language 5 is useful. to add the int we need to change that int to str and then we can replace with any other str.
# print(x.replace("python","5")) #5 is good language 5 is useful. we can replace is this way to..
# y="programming pream"
# print(y.replace("m","o",1))#prograoming pream. we can change the only one letter also.
# print(y.replace("m","o",2))#prograooing pream. we can change the only one letter also.
# print(y.replace("m","8",3))#progra88ing prea8. we can change the only one letter also.

# z="          programming         "
# print(z.strip()) #programming. this strip method is used for removing the space from both the sides from left and right side.
# print(z.lstrip()) #programming     . this method is used for removing only the left side space
# print(z.rstrip()) #         programming. this method is used for removing only the right side space

# x="              rohan        " #we need only the length of the sting so first we need to add strip and then we need to find the length.
x="              rohan        ".strip()
print(len(x))
