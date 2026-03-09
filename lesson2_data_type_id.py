from decimal import ConversionSyntax
from operator import concat

integer_var = 42
float_var = 3.14
string_var = 'Hello, Python!'
boolean_var = True

result_add = integer_var + 10
result_multiply = float_var * 2
result_concatenate= concat(string_var, 'Welcome!')
print(result_add)
print(result_multiply)
result_not_equal = boolean_var != boolean_var
print(result_not_equal)
int_to_float = ConversionSyntax(integer_var)
print(int_to_float)