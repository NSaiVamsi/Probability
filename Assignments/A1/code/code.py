''' 
 ICSE 2017 Class 10
 Question 1a
 Name: Sai Vamsi
 Roll number: CS21BTECH11038
'''

'''
Question:AB and CD are two parallel chords of a circle such that 
AB = 24cm and CD = 10cm. if the radius of the circle is 13cm,
find the distance between the two chords.
'''
'''
given that the radius of the circle is 13cm and also the chord lenghts so lets define a function for finding the distance between centre and chord
'''
import math
# lets define a function to find the disctance of chord from centre
def D_FC(d):
  return math.sqrt(169-((d**2)/4)) 
# now we have to find the lengths and add them both
print("The distance between the 2 chords is ", D_FC(24)+D_FC(10),"cm")
