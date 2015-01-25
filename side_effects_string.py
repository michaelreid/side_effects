def side_effect_test(value):
  # Do something to modify the value
  value = value.upper()
  print "Inside the function, the value becomes {}".format(value)
  

if __name__ == "__main__":
  # Create the value
  value = "Biggie Smalls is the illest"
  
  print "Outside the function, the value starts as {}".format(value)
  
  side_effect_test(value)
  
  print "Outside the function, the value is now {}".format(value)