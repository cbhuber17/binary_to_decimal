# Coding Club # Binary to Decimal

The third challenge as part of the [Coding Club](https://teams.microsoft.com/l/team/19%3aQjxVFz5CwSOZ0nKM9tUXDfMh5xLaqD_Jn5hwdVgqEEs1%40thread.tacv2/conversations?groupId=1a34467b-4e60-461c-a845-202847e59a20&tenantId=1b16ab3e-b8f6-4fe3-9f3e-2db7fe549f6a) is to create a program in any language to do the following:


In this problem we will explore two important concepts: base conversion and twos complement.  For positive numbers, converting from binary to decimal is relatively straightforward.  Negative numbers in binary are stored in a system called two’s complement.  Two’s complement is a way to store negative numbers that makes them easier to add and subtract with other numbers in binary.  In two’s complement the first bit indicates if the value is positive or negative.  To convert from positive to negative, subtract one and then invert all the bits (all 1s become 0s and all 0s become 1s).   


For example, the following shows the binary twos complement representation for a 4 bit number:  

 | Decimal | Binary |
| ------- | ------ |
| \-8     | 1000   |
| \-7     | 1001   |
| \-6     | 1010   |
| \-5     | 1011   |
| \-4     | 1100   |
| \-3     | 1101   |
| \-2     | 1110   |
| \-1     | 1111   |
| 0       | 0000   |
| 1       | 0001   |
| 2       | 0010   |
| 3       | 0011   |
| 4       | 0100   |
| 5       | 0101   |
| 6       | 0110   |
| 7       | 0111   |


Let’s look at an example: To get a value for -5, invert the binary value of positive 5 minus 1.   

5-1 = 4 -> 0100 

Inverted 4 gives 1011, which is -5.  

If you understand twos complement, then you can see why ranges for signed data types have one additional negative value than positive value.   

For example, in C++ a short int (2 bytes) ranges from -32768 to 32767.  Notice how there is one more negative number than positive number.  

Example 1:  

Enter a number in binary: 0010 

2 

Example 2:  

Enter a number in binary: 1010 

-6 

For more information about negative numbers in binary, check out this video: https://www.youtube.com/watch?v=4qH4unVtJkE