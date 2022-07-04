
## Proyect AirBnB Clone - The console 💻

#### Challenge: Write a command interpreter to manage your AirBnB objects.

```
  Resume of functionalities:
  - Create a new object (ex: a new User or a new Place)
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
### Tasks:

|       | Mandatory tasks    |
| :-------- | :------- |
| [x] | `0. README, AUTHORS` | 
| [x] | `1. Be Pycodestyle compliant!` |
| [x] | `2. Unittests` |
| [x] | `3. BaseModel` | 
| [x] | `4. Create BaseModel from dictionary` | 
| [x] | `5. Store first object` |
| [x] | `6. Console 0.0.1` |
| [x] | `7. Console 0.1` |
| [x] | `8. First User` |
| [x] | `9. More classes!` |
| [x] | `10. Console 1.0` |

|       | Advanced tasks    |
| :-------- | :------- |
| [x] | `11. All instances by class name` |
| [x] | `12. Count instances` |
| [x] | `13. Show` |
| [x] | `14. Destroy` |
| [x] | `15. Update` |
| [x] | `16. Update from dictionary` |
| [] | `17. Unittests for the Console!` |


### Commands: 📄

| Command | Example    | Description                       |
| :-------- | :------- | :-------------------------------- |
| `create`      | `create User` | Creates a new instance, print its **`id`** |
| `show`      | `show BaseModel 'valid_id'` /  `BaseModel.show("'valid_id'")` | Prints the string representation of an instance |
| `destroy`      | `destroy City 'valid_id'` / `City.destroy("'valid_id'")`| Deletes an instance |
| `all`      | `all` / `all User` /  `User.all()`| Prints all string representation of all instances |
| `update`      | `update BaseModel 'valid_id' email "aibnb@mail.com"` / `BaseModel.update("'valid_id'", "email", "aibnb@mail.com")` / `BaseModel.update("'valid_id'", {'email' : "aibnb@mail.com", 'age': 23})`|  Updates an instance |
| `count`      | `User.count()` |  Prints the number of instances of a class |

#### Classes:
```
BaseModel, User, State, City, Amenity, Place, Review
```

### Tests:

Execute:
    ```
    python3 -m unittest discover tests
    ```



## Authors

- [@IperEnma](https://github.com/IperEnma)
- [@EugeniaMatto](https://github.com/EugeniaMatto)
