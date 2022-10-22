# Base Conversion

## Introduction
This module provides a simple way to convert numbers from one base to another. The way these numbers are represented can also be changed by providing a set of symbols that are used to represent different values of each place value.

## Details
The module provides a single function: the ```convert()``` function, which takes in 5 parameters:
* ```base1```: Specifies the base that the input ```num``` is provided in.

* ```base2```: Specifies the desired base that the input ```num``` will be converted to.

* ```num```: The input provided in base ```base1```.

* ```data1```: The set of symbols for ```base1```. This should contain at least ```base1``` unique characters.

* ```data2```: The set of symbols for ```base2```. This should contain at least ```base2``` unique characters.

If ```data1``` or ```data2``` are not specified, then one of the following will occur:
* If the corresponding specified base is at most 10, then the normal base 10 digits will be used up to the given base. For example, if ```base1``` is ```3``` , but ```data1``` is not specified, then data1 will be set to ```"012"```.

* If the corresponding base is greater than 10, then the function will terminate and return an error code of either -1 or -2, depending on which ```data``` parameter was unspecified. For example, if ```base2``` is given as ```12```, but ```data2``` is not specified, an error code of ```-2``` will be returned.
### Error Codes
```convert()``` will return one of several error codes if the inputs are invalid. The error codes are given in the form of negative integers, ranging from ```-1``` to ```-7```. These error codes are determined as follows:

* ```-1``` is returned if ```base1``` is greater than 10 and ```data1``` is unspecified.

* ```-2``` is returned for the same reasons as ```-1```, except for ```base2``` and ```data2```.

* ```-3``` is returned if any of the characters in ```num``` are not found in ```data1```, since the value of that character is not defined.

* ```-4``` is returned if ```data1``` does not contain enough characters to represent all values up to but not including ```base1```.

* ```-5``` is returned for the same reasons as ```-4```, except for ```base2``` and ```data2```.

* ```-6``` is returned if ```data1``` contains repeated characters.

* ```-7``` is returned if ```data2``` contains repeated characters.

Note: These conditions are checked in the order given above, so if ```-1``` is returned, for example, that does not necessarily mean that none of the other errors are not there.

These error codes can be used in more complicated programs that incorporate user input and may have to deal with invalid inputs without throwing errors.

### Converting Process
```convert()``` first changes the input string into base 10, so that it can be stored as an ```int``` object. Then, this base 10 number is converted into the desired base using a series of Euclidean divisions as described [here](https://en.wikipedia.org/wiki/Positional_notation#Base_conversion).

## Purpose
Base conversion can be used to compress long strings of characters into many less. The most common example of this is base64. With base64, ASCII text can be shortened into less characters to accommodate for slow transmission times. Base64 is also used commonly in URLs to convert meaningful text into non-readable characters.