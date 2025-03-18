---
title: Python
---

# Python
- **Info**:
T
o
 
s
u
m
m
a
r
i
z
e
 
a
 
W
i
k
i
p
e
d
i
a
 
p
a
g
e
 
i
n
 
P
y
t
h
o
n
,
 
y
o
u
 
c
a
n
 
u
s
e
 
t
h
e
 
`
w
i
k
i
p
e
d
i
a
-
a
p
i
`
 
l
i
b
r
a
r
y
 
t
o
 
f
e
t
c
h
 
t
h
e
 
c
o
n
t
e
n
t
 
a
n
d
 
t
h
e
n
 
e
x
t
r
a
c
t
 
a
 
s
u
m
m
a
r
y
.
 
H
e
r
e
'
s
 
a
 
c
o
n
c
i
s
e
 
e
x
a
m
p
l
e
:




`
`
`
p
y
t
h
o
n


i
m
p
o
r
t
 
w
i
k
i
p
e
d
i
a
a
p
i




d
e
f
 
s
u
m
m
a
r
i
z
e
_
w
i
k
i
p
e
d
i
a
_
p
a
g
e
(
p
a
g
e
_
t
i
t
l
e
)
:


 
 
 
 
w
i
k
i
_
w
i
k
i
 
=
 
w
i
k
i
p
e
d
i
a
a
p
i
.
W
i
k
i
p
e
d
i
a
(
'
e
n
'
)


 
 
 
 
p
a
g
e
 
=
 
w
i
k
i
_
w
i
k
i
.
p
a
g
e
(
p
a
g
e
_
t
i
t
l
e
)


 
 
 
 


 
 
 
 
i
f
 
p
a
g
e
.
e
x
i
s
t
s
(
)
:


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
p
a
g
e
.
s
u
m
m
a
r
y


 
 
 
 
e
l
s
e
:


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
"
P
a
g
e
 
n
o
t
 
f
o
u
n
d
.
"




#
 
E
x
a
m
p
l
e
 
u
s
a
g
e


s
u
m
m
a
r
y
 
=
 
s
u
m
m
a
r
i
z
e
_
w
i
k
i
p
e
d
i
a
_
p
a
g
e
(
"
P
y
t
h
o
n
 
(
p
r
o
g
r
a
m
m
i
n
g
 
l
a
n
g
u
a
g
e
)
"
)


p
r
i
n
t
(
s
u
m
m
a
r
y
)


`
`
`




T
h
i
s
 
c
o
d
e
 
r
e
t
r
i
e
v
e
s
 
t
h
e
 
s
u
m
m
a
r
y
 
o
f
 
t
h
e
 
s
p
e
c
i
f
i
e
d
 
W
i
k
i
p
e
d
i
a
 
p
a
g
e
.
 
M
a
k
e
 
s
u
r
e
 
t
o
 
i
n
s
t
a
l
l
 
t
h
e
 
`
w
i
k
i
p
e
d
i
a
-
a
p
i
`
 
l
i
b
r
a
r
y
 
u
s
i
n
g
 
`
p
i
p
 
i
n
s
t
a
l
l
 
w
i
k
i
p
e
d
i
a
-
a
p
i
`
 
b
e
f
o
r
e
 
r
u
n
n
i
n
g
 
t
h
e
 
c
o
d
e
.
