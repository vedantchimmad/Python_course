# Bitwise operators

---
Bitwise operators are used to compare (binary) numbers:

| Operator | Name                  | Description                                                                                             | Example |
|----------|-----------------------|---------------------------------------------------------------------------------------------------------|---------|
| &        | and                   | Sets each bit to 1 if both bits are 1                                                                   | x & y   |
| bar      | or                    | Sets each bit to 1 if one of two bits is 1                                                              | x or Y  |
| ^        | xor                   | Sets each bit to 1 if only one of two bits is 1                                                         | x ^ y   |
| ~        | not                   | Inverts all the bits                                                                                    | x ~ y   |
| " >> "   | Zero fill left shift  | Shift left by pushing zeros in from the right and let the leftmost bits fall off                        | x >> y  |
| <<       | x%=3                  | Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off | x << y  |