create a virtualenvironment (optional)
install fastapi using pip install fastapi
and install a web sever pip install uvicorn
myapi2.py : this is a api for students details with crud operations and the outputs are stored in a json file in your directory
uvicorn myapi2:app --reload run this command and you will see a line like this  Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit) copy and paste this port in the browser
http://127.0.0.1:8000/docs type docs next to the port and you will see a beatiful ui like this where you can add a student , view a student by student_id , update a student record and delete a student record and you will see a beautiful ui like this

![image](https://github.com/user-attachments/assets/826eb48e-20aa-458c-b3b3-2e03ca468d1f)
