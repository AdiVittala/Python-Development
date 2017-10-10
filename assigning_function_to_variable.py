###Assigning varibales to functions###
#def greet(name):
 #   return "hello "+name

#greet_someone = greet("John")
#print (greet_someone)

###Define fucntions inside other functions
#def greet(name):
  #  def get_message():
 #       return "Hello "

 #   result = get_message()+name
 #   return result

#print (greet("John"))


### Fucntions can be passed as parameters to other functions###
#def greet(name):
 #  return "Hello " + name 

#def call_func(func):
 #   other_name = "John"
    #return other_name
  #  return func(other_name)  

#print (call_func(greet)) ### Outside function is evaluated first and then the inside function passed as argument is evaluated next


###Fucntions can return other functions (or generate fucntions as a return value)###
#def compose_greet_func():
  #  def get_message():
   #     return "Hello there!"

    #return get_message

#greet = compose_greet_func()### assigning a function to variable makes the variable a function ###
#print (greet())
#print (type (greet))



#### Read Access to outer Scope ### - Need to understand better
#def compose_greet_func(name):
 #   def get_message():
  #      return "Hello there "+name+"!"
   # print (type (get_message))
    #return get_message ### When returning a function with no arguments parenthesis need not be specified###

#greet = compose_greet_func("John")
#print (greet())


####Fucntion decorators are simply wrappers to existing functions.###
### Function wrapping the string output of another function by p tags###
### A Decorator function takes one fucntion(usually whose output we want modified, without actually changing the fucntion) 
### as an argument and returns the output to another fucntion
#def get_text(name):
 #  return "lorem ipsum, {} dolor sit amet".format(name)

#def p_decorate(func):
 #   def func_wrapper(name):
  #     return "<p>{}</p> fuck you".format(func(name))
   # return func_wrapper

#get_text = p_decorate(get_text)### This can be expressed in Python syntax as @p_decorate just before defning the function get_text

#print (get_text("John"))



###Python Decorator Syntax###
def p_decorate(func):
   def func_wrapper(name):
      return "<p>{}</p> fuck you".format(func(name))
   return func_wrapper

@p_decorate
def get_text(name):
  return "lorem ipsum, {} dolor sit amet".format(name)
print (get_text("John"))

