create a virtualenvironment (optional)
install fastapi using pip install fastapi
and install a web sever pip install uvicorn
myapi2.py : this is a api for students details with crud operations and the outputs are stored in a json file in your directory
uvicorn myapi2:app --reload run this command and you will see a line like this  Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit) copy and paste this port in the browser
http://127.0.0.1:8000/docs type docs next to the port and you will see a beatiful ui like this where you can add a student , view a student by student_id , update a student record and delete a student record and you will see a beautiful ui like this

![image](https://github.com/user-attachments/assets/826eb48e-20aa-458c-b3b3-2e03ca468d1f)

let's create a student record using POST method ![image](https://github.com/user-attachments/assets/6f15c16e-a68e-4231-a99c-79269ab67bf4)
now the student record is created ![image](https://github.com/user-attachments/assets/e6c751e2-25bc-48ec-96fe-a6a091793c8a) 
if we try to create a record with existing id it shows an error {
  "error": "Student exists"
}
now we are going to update a student record using PUT method 
i'm going to edit the record with id 5   ![image](https://github.com/user-attachments/assets/06200ba3-1fe2-4b3b-9263-9dd0465c2860)
![image](https://github.com/user-attachments/assets/2f4b4a02-7372-4b0f-acc0-db2b7680b1d6)
remove the comma in the last object because it will throw a error

now we'll see the GET method which will retrieve a particular record with student_id
![image](https://github.com/user-attachments/assets/47e246c8-7e88-4e9e-a103-2556a5469b57)

at last we will delete a particular record using student_id 
![image](https://github.com/user-attachments/assets/9f53b78c-ab41-4d8a-b267-d0fbab5670c5)

Now we can see all the students using GET method 
![image](https://github.com/user-attachments/assets/991f7988-c164-4845-95be-e0befa54fd37)







