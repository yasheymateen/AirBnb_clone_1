# AirBnB_clone
This project is one of a series that aims to make from scratch a clone of AirBnb. <hr/>

# Command Interpreter (Console)
This particular project focuses on creating a command interpreter to manage AirBnb objects.<br/>


### Models: <br/>
* BaseModel
* User
* State
* City
* Amenity
* Place
* Review


Each model is given a unique id, the 'created_at' attribute specifying when the oject was creeated, 'updated_at' specifying when the object was updated at, adn '__class__' specifiying the object's type.


### Usage: <br/>
Run ./console.py in the root directory.
```
./console.py
```

### Commands: <br/>
* update  - updates an attribute name by its 'object id' with its attribute value.
* destroy - deletes an object by its 'object id'
* create - creates an object of a specific type.
* show - displays object by its 'object id'
* all - displays all objects of a specific type
* help [command] - shows help of information of a command.

### Example:

```
(hbnb) create BaseModel
e2beccb3-166b-4862-8ac2-595b3438d5ff

(hbnb) update BaseModel e2beccb3-166b-4862-8ac2-595b3438d5ff first_name "Beyonce"

(hbnb) show BaseModel e2beccb3-166b-4862-8ac2-595b3438d5ff
[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'first_name': 'Beyonce', 'id': '49faff9a-6318-451f-87b6-910505c55907', 'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'updated_at': datetime.datetime(2017, 10, 2, 3, 11, 3, 49401)}


```


### AUTHORS

Aalaa Satti - <ala.k.satti@gmail.com><br/>
Yashar Mateen - <yasheymateen@gmail.com><br/>
