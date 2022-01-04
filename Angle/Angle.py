"""
Angle.
Author: Aden Koperczak
Date:   2022-01-04

Adds an Angle class. This is mainly just for formatting and conversion.

The angle format specifier is defined bellow:
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

Refrences:
    format_spec: https://docs.python.org/3/library/string.html#format-specification-mini-language
"""

from math import pi # pi is used to convert to and from radians

RADIANS_TO_DEGREES  = 360 / (pi * 2) # coefficient for converting from radians to degrees
RADIANS_TO_GRADIANS = 400 / (pi * 2) # coefficient for converting from radians to gradians 

class Angle(float):
    # defines the unit that the angle is stored in.
    DEFAULT_UNIT = "r"

    # defines the symboles used of each unit
    UNIT_SYMBOLS = {
        "r": "rad",
        "d": "\u00B0",
        "g": "gon"
    }

    def radians(self):
        """Convert the angle to radians, returns a float."""
        return float(self)

    def degrees(self):
        """Convert the angle to degrees, returns a float."""
        return float(self * RADIANS_TO_DEGREES)

    def gradian(self):
        """Convert the angle to gradians, returns a float."""
        return float(self * RADIANS_TO_GRADIANS)

    def DMS(self):
        """Convert the angle to degrees minutes seconds, returns a tuple of floats."""
        secs = self.degrees() * 3600
        mins, secs = divmod(secs, 60)
        degs, mins = divmod(mins, 60)

        return degs, mins, secs
        

    def __format__(self, spec):
        """Format the output given the format spec"""
        fullSpec = spec            # save the full spec for use in error messages
        value = float(self)        # The default value is simply the number the angle is stored as 
        unit  = self.DEFAULT_UNIT  # The default unit is well, the default unit.

        # check for unit specification
        if len(spec) > 1 and spec[1] == ":":
            unit = spec[0]
            # set the value according to the unit, or raise an error on invalid input.
            match unit:
                case "r":
                    value = self.radians()
                case "d":
                    value = self.degrees()
                case "g":
                    value = self.gradian()
                case "D":
                    value = self.DMS()
                case _:
                    ValueError(f"Invalid format specifier for Angle: '{fullSpec}'. '{spec[0]}' is not a valid angle conversion")
            spec = spec[2:] # remove unit specification from the output.

        # The text to output for the unit
        unitText = ""

        if len(spec) > 0:
            # check what (if any) unit format should be output
            match spec[-1]:
                case "u":
                    unitText = unit
                case "U":
                    unitText = self.UNIT_SYMBOLS.get(unit, "")
            if unitText != "":
                spec = spec[:-1]

        # get the alignment feild
        alignment = ""
        if len(spec) > 0 and spec[0] == "(":
            # find the ending ")" and error if none 
            end = spec.find(")")
            if end == -1:
                raise ValueError(f"Invalid format specifier for Angle: '{fullSpec}'. Unmached '(' in alignment.")
            
            # get the alignment text itself, and remove it from spec.
            alignment = spec[1:end]
            spec = spec[end + 1:]

        if unit == "D":
            # DMS D and M are both ints, format secs.
            degs = str(int(value[0]))
            mins = str(int(value[1]))
            secs = format(value[2], spec)

            # allways output with units. (otherwise output is ambiguos)
            output = f"{degs}\u00B0 {mins}' {secs}\""
        else:
            # format most output simply with this
            output = format(value, spec) + unitText
        # do the aligmentof the hole output.
        return format(output, alignment)

def Radians(number):
    """Make an angle from Radians"""
    return Angle(number)

def Degrees(number):
    """Make an angle form Degrees"""
    return Angle(float(number) / RADIANS_TO_DEGREES)

def Gradians(number):
    """Make an angle from a Gradiant"""
    return Angle(float(number) / RADIANS_TO_GRADIANS)

def DMS(degrees, minutes, seconds):
    """Make an agle form Degrees Minutes and Seconds"""
    return Degrees(float(degees) + float(minutes) / 60 + float(seconds) / 3600)



if __name__ == "__main__":
    def example_usage():
        """An example program using the Angle class. 
        Takes an angle in degrees as a user input, and outputs that angle in 
        several formats."""
        formats = [("Default", "u"), 
                   ("Radians", "r:U"), 
                   ("Degrees", "d:U"), 
                   ("Gradians", "g:U"),
                   ("Degree Minuits Seconds", "D:"),
                   ("Degrees Formatted", "d:( >10).4U")]

        try:
            while True:
                inp = input("Angle in degrees: ")
                if inp == "":
                    break
                a = Degrees(inp)
                for name, form in formats:
                    print(f"{name} '{form}':", format(a, form))
                print()
        except KeyboardInterrupt:
            pass
    example_usage()
