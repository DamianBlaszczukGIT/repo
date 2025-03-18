---
title: JavaScript
---

# JavaScript
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
S
c
r
i
p
t
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
 
M
e
d
i
a
W
i
k
i
 
A
P
I
 
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
 
o
f
 
t
h
e
 
p
a
g
e
 
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




1
.
 
U
s
e
 
t
h
e
 
F
e
t
c
h
 
A
P
I
 
t
o
 
g
e
t
 
t
h
e
 
p
a
g
e
 
c
o
n
t
e
n
t
.


2
.
 
P
a
r
s
e
 
t
h
e
 
J
S
O
N
 
r
e
s
p
o
n
s
e
.


3
.
 
E
x
t
r
a
c
t
 
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
 
f
r
o
m
 
t
h
e
 
"
e
x
t
r
a
c
t
"
 
f
i
e
l
d
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
 
c
o
d
e
 
s
n
i
p
p
e
t
:




`
`
`
j
a
v
a
s
c
r
i
p
t


a
s
y
n
c
 
f
u
n
c
t
i
o
n
 
s
u
m
m
a
r
i
z
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
P
a
g
e
(
t
i
t
l
e
)
 
{


 
 
 
 
c
o
n
s
t
 
r
e
s
p
o
n
s
e
 
=
 
a
w
a
i
t
 
f
e
t
c
h
(
`
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
a
p
i
/
r
e
s
t
_
v
1
/
p
a
g
e
/
s
u
m
m
a
r
y
/
$
{
e
n
c
o
d
e
U
R
I
C
o
m
p
o
n
e
n
t
(
t
i
t
l
e
)
}
`
)
;


 
 
 
 
c
o
n
s
t
 
d
a
t
a
 
=
 
a
w
a
i
t
 
r
e
s
p
o
n
s
e
.
j
s
o
n
(
)
;


 
 
 
 
r
e
t
u
r
n
 
d
a
t
a
.
e
x
t
r
a
c
t
;
 
/
/
 
T
h
i
s
 
c
o
n
t
a
i
n
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


}




/
/
 
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
i
z
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
P
a
g
e
(
'
J
a
v
a
S
c
r
i
p
t
'
)
.
t
h
e
n
(
s
u
m
m
a
r
y
 
=
>
 
c
o
n
s
o
l
e
.
l
o
g
(
s
u
m
m
a
r
y
)
)
;


`
`
`




T
h
i
s
 
f
u
n
c
t
i
o
n
 
f
e
t
c
h
e
s
 
a
 
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
 
a
n
d
 
l
o
g
s
 
i
t
 
t
o
 
t
h
e
 
c
o
n
s
o
l
e
.
