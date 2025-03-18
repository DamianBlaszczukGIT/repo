---
title: Java
---

# Java
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
 
u
s
i
n
g
 
J
a
v
a
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
 
l
i
b
r
a
r
i
e
s
 
l
i
k
e
 
J
s
o
u
p
 
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
 
t
h
e
 
r
e
l
e
v
a
n
t
 
t
e
x
t
.
 
H
e
r
e
'
s
 
a
 
s
i
m
p
l
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
j
a
v
a


i
m
p
o
r
t
 
o
r
g
.
j
s
o
u
p
.
J
s
o
u
p
;


i
m
p
o
r
t
 
o
r
g
.
j
s
o
u
p
.
n
o
d
e
s
.
D
o
c
u
m
e
n
t
;




p
u
b
l
i
c
 
c
l
a
s
s
 
W
i
k
i
p
e
d
i
a
S
u
m
m
a
r
y
 
{


 
 
 
 
p
u
b
l
i
c
 
s
t
a
t
i
c
 
v
o
i
d
 
m
a
i
n
(
S
t
r
i
n
g
[
]
 
a
r
g
s
)
 
{


 
 
 
 
 
 
 
 
t
r
y
 
{


 
 
 
 
 
 
 
 
 
 
 
 
S
t
r
i
n
g
 
u
r
l
 
=
 
"
h
t
t
p
s
:
/
/
e
n
.
w
i
k
i
p
e
d
i
a
.
o
r
g
/
w
i
k
i
/
J
a
v
a
_
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
_
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
;


 
 
 
 
 
 
 
 
 
 
 
 
D
o
c
u
m
e
n
t
 
d
o
c
 
=
 
J
s
o
u
p
.
c
o
n
n
e
c
t
(
u
r
l
)
.
g
e
t
(
)
;


 
 
 
 
 
 
 
 
 
 
 
 
S
t
r
i
n
g
 
s
u
m
m
a
r
y
 
=
 
d
o
c
.
s
e
l
e
c
t
(
"
p
"
)
.
f
i
r
s
t
(
)
.
t
e
x
t
(
)
;
 
/
/
 
G
e
t
 
t
h
e
 
f
i
r
s
t
 
p
a
r
a
g
r
a
p
h


 
 
 
 
 
 
 
 
 
 
 
 
S
y
s
t
e
m
.
o
u
t
.
p
r
i
n
t
l
n
(
s
u
m
m
a
r
y
)
;


 
 
 
 
 
 
 
 
}
 
c
a
t
c
h
 
(
E
x
c
e
p
t
i
o
n
 
e
)
 
{


 
 
 
 
 
 
 
 
 
 
 
 
e
.
p
r
i
n
t
S
t
a
c
k
T
r
a
c
e
(
)
;


 
 
 
 
 
 
 
 
}


 
 
 
 
}


}


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
 
f
e
t
c
h
e
s
 
t
h
e
 
J
a
v
a
 
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
 
a
n
d
 
p
r
i
n
t
s
 
t
h
e
 
f
i
r
s
t
 
p
a
r
a
g
r
a
p
h
 
a
s
 
a
 
s
u
m
m
a
r
y
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
c
l
u
d
e
 
t
h
e
 
J
s
o
u
p
 
l
i
b
r
a
r
y
 
i
n
 
y
o
u
r
 
p
r
o
j
e
c
t
 
t
o
 
r
u
n
 
t
h
i
s
 
c
o
d
e
.
