# Logiacal operator
# ----------------

# AND

#

# i/p    o/p
# 0,0     0
# 0,1     0
# 1,0     0
# 1,1     1

#  2 :- 0010   (converting to binary)
#  4 :- 0100
#       ----
#       0000 => 0 (corresponding value)

num1=2
num2=4

print(num1&num2)

num1=4
num2=4

print(num1&num2)

num1=4
num2=6

print(num1&num2)

num1=4
num2=3

print(num1&num2)

#................................................

# OR

#

# i/p    o/p
# 0,0     0
# 0,1     1
# 1,0     1
# 1,1     1

num1=2               # 2 :- oo1o
num2=6               # 6 :- 0110
                     #   :- 0110  => 6

print(num1|num2)     # => 6 (output)



num1=8               # 8 :- 1o0o
num2=6               # 6 :- 0110
                     #   :- 1110  => 14

print(num1|num2)     # => 14 (output)

#......................................................

# XOR

# XOR Gate :-

# i/p    o/p
# 0,0     0
# 0,1     1
# 1,0     1
# 1,1     0

num1=2               # 2 :- oo1o
num2=6               # 6 :- 0110
                     #   :- 0100  => 4

print(num1^num2)     # => 4 (output)