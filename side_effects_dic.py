def side_effect_test(value):
  # Do something to modify the value
  value[1] = "Jay-z"
  print "Inside the function, the value becomes {}".format(value)
  

if __name__ == "__main__":
  # Create the value
  value = {1:"Biggie", 2:"NAS", 3:"Clipse"}
  
  print "Outside the function, the value starts as {}".format(value)
  
  side_effect_test(value)
  
  print "Outside the function, the value is now {}".format(value)