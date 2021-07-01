# 0x00. AirBnB clone - The console
_Foundations > Higher-level programming > AirBnB clone_

By Guillaume, CTO at Holberton School

Authors: [Carlos Andres Polania](https://twitter.com/timberdev),
[Oscar Angel](https://twitter.com/eloskyA)

## Learning Objectives


How to create a Python package
-   How to create a command interpreter in Python using the  `cmd`  module
-   What is Unit testing and how to implement it in a large project
-   How to serialize and deserialize a Class
-   How to write and read a JSON file
-   How to manage  `datetime`
-   What is an  `UUID`
-   What is  `*args`  and how to use it
-   What is  `**kwargs`  and how to use it
-   How to handle named arguments in a function

![Airbnb Console](https://holbertonintranet.s3.amazonaws.com/uploads/medias/2018/6/815046647d23428a14ca.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUWMNL5ANN/20210630/us-east-1/s3/aws4_request&X-Amz-Date=20210630T203434Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=82db87b684c4c96f8e548db9179f5f6bc41078491079c3f96cd21ced654e8b89)


### How to start it?

    git clone https://github.com/capolaniaq/AirBnB_clone.git
    cd AirBnB/
    ./console.py


### How to use interactive mode:
### command usage
- create `class name`
- show  `class name` `id`
- destroy `class name` `id`
- all
- all `class name`
- update `class name` `id` `attribute name` `attribute value`

#### examples

    (hbnb) help

	Documented commands (type help <topic>):

	========================================

	EOF help quit

	(hbnb)
	(hbnb)
	(hbnb)

### Examples

    (hbnb) create BaseModel
    8800b9d6-c42b-432c-a1e0-be8397b03159
    (hbnb) show BaseModel 8800b9d6-c42b-432c-a1e0-be8397b03159
    [BaseModel] (8800b9d6-c42b-432c-a1e0-be8397b03159) {'created_at': datetime.datetime(2021, 7, 1, 2, 17, 43, 210804), 'updated_at': datetime.datetime(2021, 7, 1, 2, 17, 43, 210850), 'id': '8800b9d6-c42b-432c-a1e0-be8397b03159'}
    (hbnb) update BaseModel 8800b9d6-c42b-432c-a1e0-be8397b03159 name School
    (hbnb) show BaseModel 8800b9d6-c42b-432c-a1e0-be8397b03159
    [BaseModel] (8800b9d6-c42b-432c-a1e0-be8397b03159) {'created_at': datetime.datetime(2021, 7, 1, 2, 17, 43, 210804), 'updated_at': datetime.datetime(2021, 7, 1, 2, 19, 6, 920983), 'id': '8800b9d6-c42b-432c-a1e0-be8397b03159'}


### How to use non-interactive mode:

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