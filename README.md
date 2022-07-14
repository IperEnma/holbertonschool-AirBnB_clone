## Proyect AirBnB Clone - The console 💻

#### Challenge: Write a command interpreter to manage your AirBnB objects.

```
  Resume of functionalities:
  -  Create a new object (ex: a new User or a new Place)
  -  Retrieve an object from a file, a database etc…
  -  Do operations on objects (count, compute stats, etc…)
  -  Update attributes of an object
  -  Destroy an object
```
### How to use:
Execute:
      ```
        ./console.py
      ```
### Commands: 📄

| Command | Example    | Description                       |
| :-------- | :------- | :-------------------------------- |
| `create`      | `create User` | Creates a new instance, print its **`id`** |
| `show`      | `show BaseModel 'valid_id'` /  `BaseModel.show("'valid_id'")` | Prints the string representation of an instance |
| `destroy`      | `destroy City 'valid_id'` / `City.destroy("'valid_id'")`| Deletes an instance |
| `all`      | `all` / `all User` /  `User.all()`| Prints all string representation of all instances |
| `update`      | `update BaseModel 'valid_id' email "aibnb@mail.com"` / `BaseModel.update("'valid_id'", "email", "aibnb@mail.com")` / `BaseModel.update("'valid_id'", {'email' : "aibnb@mail.com", 'age': 23})`|  Updates an instance |
| `count`      | `User.count()` |  Prints the number of instances of a class |
| `help`      | `help` /  `help Create`|  Help |
| `quit`      | `quit` |  Exit the program |

#### Supported Classes:
```
BaseModel, User, State, City, Amenity, Place, Review
```

### How does it works:

- Interactive Mode:
```
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$
```

- Non-interactive mode:
```
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
```

### Tests:
All tests should also pass in non-interactive mode.

Execute:  
  ```
    python3 -m unittest discover tests
    ```
### Tasks:

|       | Mandatory tasks    |
| :-------- | :------- |
| ✓ | `0. README, AUTHORS` | 
| ✓ | `1. Be Pycodestyle compliant!` |
| ✓ | `2. Unittests` |
| ✓ | `3. BaseModel` | 
| ✓ | `4. Create BaseModel from dictionary` | 
| ✓ | `5. Store first object` |
| ✓ | `6. Console 0.0.1` |
| ✓ | `7. Console 0.1` |
| ✓ | `8. First User` |
| ✓ | `9. More classes!` |
| ✓ | `10. Console 1.0` |

|       | Advanced tasks    |
| :-------- | :------- |
| ✓ | `11. All instances by class name` |
| ✓ | `12. Count instances` |
| ✓ | `13. Show` |
| ✓ | `14. Destroy` |
| ✓ | `15. Update` |
| ✓ | `16. Update from dictionary` |
| X | `17. Unittests for the Console!` |


## Authors

- [@IperEnma](https://github.com/IperEnma)
- [@EugeniaMatto](https://github.com/EugeniaMatto)

<h1 align="center">Hi 👋, I'm IperEnma</h1>
<p align="left"> <img src="https://komarev.com/ghpvc/?username=iperenma&label=Profile%20views&color=0e75b6&style=flat" alt="iperenma" /> </p>

- 🌱 I’m currently learning **JAVA, C, Python, MySQL**

- 📫 How to reach me **enmanuelhernandez1843@gmail.com**

<h3 align="left">Connect with me:</h3>
<p align="left">
<a href="https://linkedin.com/in/enmanuel-h-a382b2121" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/linked-in-alt.svg" alt="enmanuel-h-a382b2121" height="30" width="40" /></a>
</p>

<h3 align="left">Languages and Tools:</h3>
<p align="left"> <a href="https://www.gnu.org/software/bash/" target="_blank" rel="noreferrer"> <img src="https://www.vectorlogo.zone/logos/gnu_bash/gnu_bash-icon.svg" alt="bash" width="40" height="40"/> </a> <a href="https://www.cprogramming.com/" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/c/c-original.svg" alt="c" width="40" height="40"/> </a> <a href="https://git-scm.com/" target="_blank" rel="noreferrer"> <img src="https://www.vectorlogo.zone/logos/git-scm/git-scm-icon.svg" alt="git" width="40" height="40"/> </a> <a href="https://www.java.com" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/java/java-original.svg" alt="java" width="40" height="40"/> </a> <a href="https://www.linux.org/" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/linux/linux-original.svg" alt="linux" width="40" height="40"/> </a> <a href="https://www.mysql.com/" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/mysql/mysql-original-wordmark.svg" alt="mysql" width="40" height="40"/> </a> <a href="https://www.python.org" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="python" width="40" height="40"/> </a> </p>
