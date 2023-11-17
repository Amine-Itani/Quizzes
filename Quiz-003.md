# Quiz 003
## Protein Converter
I found this quiz pretty cool because it connected with real life examples and uses
We learned to use functions in this exercise as well, which really helped me keep everything organized
It was a little tough in the beginning though, as can be seen from all the scribbles
This quiz took in inputs (proteins) in "ATGC" and converts them to "TACG" respectively

## Code

```py
def translator(in_protein:str)->str:
    output = ""
    for protein in in_protein:
        if protein == "A":
            output += "T"
        elif protein == "G":
            output += "C"
        elif protein == "T":
            output += "A"
        else:
            output += "G"
    return output

case1 = translator("AGTCTGGCTGA")
print(case1)
```

## Evidence
![image](https://github.com/Amine-Itani/Unit-1/assets/123438294/7384be1b-71ed-41c4-8c5a-60a01513ab12)

<sub>Fig.1 shows results of the program

## Flowchart
![Quiz003](https://github.com/Amine-Itani/Unit-1/assets/123438294/d6a14c2c-7e33-4278-9dad-087fd1889ffa)
<sub>Fig.2 shows results of the program
