
"""
String Formatting Operator
One of Python's coolest features is the string format operator %. This operator is unique to strings and makes up for the pack of having functions from C's printf() family. Following is a simple example −
Here is the list of complete set of symbols which can be used along with % −

S.No.	Format Symbol & Conversion
1	
%c

character

2	
%s

string conversion via str() prior to formatting

3	
%i

signed decimal integer

4	
%d

signed decimal integer

5	
%u

unsigned decimal integer

6	
%o

octal integer

7	
%x

hexadecimal integer (lowercase letters)

8	
%X

hexadecimal integer (UPPERcase letters)
9	
%e

exponential notation (with lowercase 'e')

10	
%E

exponential notation (with UPPERcase 'E')

11	
%f

floating point real number

12	
%g

the shorter of %f and %e

13	
%G

the shorter of %f and %E

Other supported symbols and functionality are listed in the following table −

S.No.	Symbol & Functionality
1	
*

argument specifies width or precision

2	
-

left justification

3	
+

display the sign

4	
<sp>

leave a blank space before a positive number

5	
#

add the octal leading zero ( '0' ) or hexadecimal leading '0x' or '0X', depending on whether 'x' or 'X' were used.

6	
0

pad from left with zeros (instead of spaces)

7	
%

'%%' leaves you with a single literal '%'

8	
(var)

mapping variable (dictionary arguments)

9	
m.n.

m is the minimum total width and n is the number of digits to display after the decimal point (if appl.)"""

print ("My name is %s and weight is %d kg!" % ('Zara', 21))
