# Angle
This program simply implements a class that can be used to convert angles 
between diffrent units and format an angle using pythons formatting system.

## Overview
The Angle class does not add anything in terms of doing math on angles. It is
primarly a class to allow for easier formatting. It is a subclass of float, so
many mathmatical operations work with it (although the output will likely be a 
float not an Angle). The only real additions are the conversion functions and
methodes, and the formatting syntax.

## Conversion Functions.
There are four conversion functions, each of which can be used to make an angle.
These are Radians, Degrees, Gradians, and DMS. These each convert from their
respecive unit, to an Angle. Note that the value of an angle is stored in 
Radians.

## Conversion Methodes
There are four conversion methodes, each of convert an angle into a float.
These are radians, degrees, gradians, and DMS. These each convert to their
respecive unit, from an Angle.

## Formatting
The main goal of this programm was to add the formatting, so it is the most
complicated part. By overriding the __format__ method of Angle, an extensive 
format specification was added to the class. Bellow is the specification:

```
angle_spec  ::= [unit:][(alignment)][number][unitDisplay]
unit        ::= "r" | "d" | "g" | "D"
alignment   ::= format_spec 
number      ::= format_spec
unitDisplay ::=  "u" | "U"

The unit field describes the unit the output should be in. Its values represent 
the following units
"r": radians,
"d": degrees,
"g": gradians,
"D": degrees minutes seconds

The alignment field consists of the standard format_spec for a string. This is
indended to allow for the use of the fill, align, and width fields to the whole
string.

The number field consists of the standard format_spec for a number. This is used
to format the numeric output of the output. This is primarly intended for formatting
presission and other numeric only constants.
For degrees minutes seconds, the number field is only used for the seconds.
The fill option cannot be "(" as that indicates an alignment option.

The unitDisplay field specifies if and how a unit should be added to the output.
This field does nothing with degrees minutes seconds because units are 
always used. 
"":  no unit representation.
"u": display a letter representation of the unit.
"U": display the symbol of the unit.
```

More can be learned about Python's format specification at Pythons website
(https://docs.python.org/3/library/string.html#format-specification-mini-language)
