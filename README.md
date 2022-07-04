
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
