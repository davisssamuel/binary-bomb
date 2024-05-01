# Phase 1

In Ghidra, I opened the `phase_1` function I immediately saw that the function was comparing the input against the string `Verbosity leads to unclear, inarticulate things.`

# Phase 2

Opening the `phase_2` function I immediately saw the function `read_six_numbers` so I knew my input would be 6 numbers. I noticed the first conditional checked if the first number in the input was a 1. 

```c
do {
	if (piVar1[1] != *piVar1 * 2) {
		explode_bomb();
	}
	piVar1 = piVar1 + 1;
} while (piVar1 != local_38 + 5);
```

Examining the following do-while loop, I noticed each iteration checked if `piVar1` was double itself. `piVar1` is a point to whatever is stored in the variable `local_38`, which is where the user input is stored. 

```c
do {
	if (piVar1[1] != *piVar1 * 2) {
		explode_bomb();
	}
	piVar1 = piVar1 + 1;
} while (piVar1 != local_38 + 5);
```

So, I concluded this phase checked for 6 numbers, each one being double the last; for me these numbers were `1 2 4 8 16 32`.

# Phase 3

Opening the `phase_3` function I noticed the first conditional checked if the length of the input was 3. Then I noticed the switch statement checked the first input. Each case of the switch statement set `cVar1` to a specific character and then checked if the third input, `local_14`, was equal to a predetermined number. In case 0, the `cVar1` gets set to `z` and then checks if the third input is the number 208.

```c
case 0:
	cVar1 = 'z';
	if (local_14 != 0xd0) {
		explode_bomb();
		cVar1 = 'z';
    }
    break;
```

Finally, the second input is checked against `cVar1`. Based on case 0, the second input should be `z`. There are at least 8 successful inputs based on the 8 cases in the switch statement, but for case 0, the full input was `0 z 208`.

# Phase 4

Opening the `phase_4` function, I immediately saw the function `func4` and knew it would be an integral part of defusing this phase. Examining `func4`, I saw the function was getting the midpoint between the last two parameters, in my case, 0 and 14, and then calling itself recursively based on if the midpoint was greater or less than the first parameter which is the first input, or `local_18`. Looking back at `phase_4`, I noticed `iVar1` is set to the output of `func4`. The function then checks if `iVar 1` and the second input, `local_14`, is equal to 37. I figured the easiest way to determine what the first input should be was to recreate the function in Python and the iterate through inputs until I received a 37. The full input was `10 37`.

```python
# func4.py

def func4(param_1, param_2, param_3):
  iVar1 = 0
  iVar2 = (param_3 - param_2) / 2 + param_2
  if (param_1 < iVar2):
    iVar1 = func4(param_1, param_2, iVar2 + -1)
    iVar2 = iVar2 + iVar1
  elif (iVar2 < param_1):
    iVar1 = func4(param_1, (iVar2 + 1), param_3)
    iVar2 = iVar2 + iVar1
  return iVar2

x = 0
while func4(x, 0, 14) != 37:
  x += 1
print(x)
```

# Phase 5

Opening the `phase_5` function, I immediately saw the another do-while loop and begin examining there. I was unfamiliar with the C syntax for the `local_18` assignment, so I had ChatGPT explain it; the assignment was finding the value in `array.3472` at index `local_18 * 4`. Every time this loop iterated, it would use the array value from the last iteration,  `local_18`, multiplied by four, to assign a new value to `local_18`.  It would also add the value of `local_18` to `iVar1`. Only if `iVar2` equaled 15 and the second input, `local_14`, was equal to `iVar1` would the phase be defused. I was struggling to debug the execution with gdb, so I created a brute force Python script to help me. The input to defuse this phase was `5 115`.

```c
do {
	iVar2 = iVar2 + 1;
	local_18 = *(uint *)(array.3472 + (long)(int)local_18 * 4);
	iVar1 = iVar1 + local_18;
} while (local_18 != 0xf);
```

# Phase 6

Similar to the last phase, I was struggling to debug the execution. I noticed the `read_six_numbers` function, so I knew there would be six integer inputs. Ultimately, I used the brute force script I wrote in the last phase to find the input to defuse this phase. The input to defuse this phase was `4 5 1 6 3 2`.
