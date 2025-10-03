# format specifier = {value: flags} 
#     ---> format a value based on what flags are specified.

# 1.  .(number)f --> round to that many decimal places(fixed point)
# 2.  :(number) ---> allocate that many spaces
# 3.  :03     -----> allocate and zero pad that many spaces
# 4.  :<      -----> left justify
# 5.  :>      -----> right justify
# 6.  :^      -----> center align
# 7.  :+      -----> add a plus sign to indicate +ve Value
# 8.  :=      -----> place sign to leftmost position
# 9.  :       -----> insert a space before +ve numbers
# 10. :,      -----> comma seperator

value1 = 848.3489300
value2 = -349.340983
value3 = 939.990

#Round decimal places[]
print(f"value1 upto 2 float: {value1:.2f}") #value1 upto 2 float: 848.35
print(f"value2 upto 1 float: {value2:.1f}") #value2 upto 1 float: -349.3
print(f"value3 upto 3 float: {value3:.3f}") #value3 upto 3 float: 939.990

#allocate {n} spaces 
print(f"value1 add space: {value1:10}")  #value1 add space:  848.34893
print(f"value2 spaces with 2f: {value2:10.2f}") #value2 spaces with 2f:    -349.34
print(f"value3 of 1f and 6 space: {value3:6.1f}") #value3 of 1f and 6 space:  940.0


#allocate and zero pad {n} spaces
#add 0 before a number if it has less digit than {n}.
print(f"value1: {value1:010.2f}") #value1 :0000848.35
print(f"value2: {value2:012.1f}") #value2: -000000349.3
print(f"value3 no .f: {value3:012}") #value3 no .f: 000000939.99

#Left & Right Justify and center align
print(f"value1 left justify: {value1:<}") #by default
print(f"value2 right justify 10space: {value2:>10.1f}") #value2 right justify 10space:     -349.3
print(f"value3 center align 012space 2f: {value3:^012.2f}") #value3 center align 12space 1f: 000939.99000


# add plus sign before +ve value
print(f"value1 add + if +ve value: {value1:+}")
print(f"value2 add + if +ve value: {value2:+}")
print(f"value3 add + if +ve value: {value3:+}")

#comma seperator
print(f"88247823.834838 with comma: {88247823.834838:,}") #88247823.834838 with comma: 88,247,823.834838