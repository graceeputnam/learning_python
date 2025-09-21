# Final Live-Coding Exam

## Instructions

Pick **one** of the following problems to solve.
Submit the file you implemented to gradescope. 
Do **not** submit the other files.

## Problems (pick one)

### 1. Manufacturing

Write code for this problem in `check_build.py`.

You have a CSV file that contains the
inventory of a set of parts. You also have a CSV file
that lists a set of parts for a "build", meaning the
quantity of each part needed to build a particular project.
Print out any parts from the build that lack sufficient inventory,
indicating how many parts need to be ordered to complete the build.

In the inventory, the columns are: PART-NUMBER, DESCRIPTION, and QUANTITY

**inventory.csv**

```
ELEC-001,Resistor 10kΩ,15
ELEC-002,Capacitor 100μF,30
ELEC-005,Diode 1N4007,17
MECH-001,Heat Sink Aluminum,56
ELEC-012,LED Red 5mm,77
ELEC-013,LED Green 5mm,42
CTRL-003,Arduino Nano,74
CTRL-004,Arduino Uno,45
```

In the build, the columns are: PART-NUMBER and QUANTITY

**build.csv**

```
CTRL-004,1
ELEC-001,20
ELEC-002,10
MECH-001,2
ELEC-005,20
ELEC-012,5
```

Following is an example of running `check_build.py`. The program
takes two arguments, first the inventory file and second the build file.

```bash
python check_build.py inventory.csv build.csv
The following parts need to be ordered
PART: QUANTITY LACKING
----------------------
ELEC-001: 5
ELEC-005: 3
----------------------
```

### 2. Natural Language Processing (NLP)

Write code for this problem in `remove_frequent.py`.

Words that occur frequently (known as "stop words")
are often not interesting in certain language-analysis problems.

Write a program that (1) removes all words from a file
that appear as many or more times as the provided threshold
and (2) writes the remaining words to the specified file.

Ignore case and punctuation.

The output words should all be lowercase and have no punctuation, 
separated by spaces, all on one line.

Here is an example of a file containing words:

**words.txt**

```text
I want a cat. 
I want a DOG. 
I do not want a bird.
A BIRD I do NOT want.
```

Following is an example of running `remove_frequent.py`. The program
takes three arguments, first the threshold for stop words, second
the words file, and third an output file. In this case, 3 means remove
all words that appear 3 or more times in the input file.

```bash
python remove_frequent.py 3 words.txt output.txt
```

**output.txt**

```text
cat dog do not bird bird do not
```

### 3. Business Analytics

Write code for this problem in `analyze_logs.py`.

On the internet, each machine is identified by an IP address (e.g. `128.187.83.1`).
For this problem, we will say that the first number of the IP address loosely
correlates with a region of the world. For the above address, the region is 128.

Servers can be configured to log the IP address of each computer that tries to connect to it.
By analyzing these IP addresses, you can get an idea of where in the world your server traffic is originating.

Write a program that takes a server contact log and prints out a summary that identifies
the region with the maximum number of connections (i.e. the greatest degree of traffic).

An example of a log file is shown below. 
There are two entries on each line,
a time stamp and an IP address, separated by a space.

**log.txt**

```text
2024-11-25T10:45 128.187.83.1    
2024-11-25T10:46 68.10.16.10  
2024-11-25T10:47 128.187.83.2  
2024-11-25T10:47 68.10.16.10   
2024-11-25T10:48 32.84.12.128
2024-11-25T10:49 68.10.16.2   
2024-11-25T10:51 68.10.16.8   
2024-11-25T10:53 32.84.12.128
2024-11-25T10:47 128.187.83.2  
```

Following is an example of running `analyze_logs.py`. 
The program takes one argument: the name of the log file.

```bash
python analyze_logs.py ip_logs.txt
Region 68 had 4 connections.
```

## Reference

Here are a few snippets of python code to remind you of syntax and options:

```python
def read_lines(filename):
    with open(filename) as file:
        return file.readlines()
    
def read_content(filename):
    with open(filename) as file:
        return file.read()
    
def write_lines(filename, lines_to_write):
    with open(filename, 'w') as file:
        file.writelines(lines_to_write)
        
def write_content(filename, content):
    with open(filename, 'w') as file:
        file.write(content)
```

```python
from string import punctuation
# punctuation is a string with all the punctuation characters in it
```

```python
if __name__ == '__main__':
# Call your main function here
```