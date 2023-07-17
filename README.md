# Health Management System

The Health Management System is a command-line application that allows you to conveniently manage your exercise and diet data. With this system, you can easily add and retrieve information about your physical activities and meals to help you maintain a healthy lifestyle.

## Features

- **Add exercise data**: You can add details about your exercise routine by specifying your name, the type of exercise, and the date/time when it was performed. The data will be stored in a text file named after you.

- **Add diet data**: Keep track of your meals by providing information such as your name, the food consumed, and the date/time of the meal. The system will store this information in a text file dedicated to you.

- **Retrieve exercise data**: Retrieve exercise data for any specific person. The system will display the exercise details along with the corresponding date and time.

- **Retrieve diet data**: Retrieve diet data for any specific person. The system will display the food consumed along with the corresponding date and time.

## How to Use

1. Run the `health_management_system.py` file to launch the application.

2. Choose the operation you want to perform: adding data or retrieving data.

3. Select whether you want to add/retrieve exercise or diet data.

4. Choose the person for whom you want to add/retrieve data (e.g., Rahul, Raj, Rohan).

5. Follow the prompts to provide the necessary details for the selected operation.

6. The system will store or display the data accordingly.

## File Structure

- `health_management_system.py`: This is the main Python file that contains the logic for the Health Management System.

- `<person_name> exercise.txt`: This text file stores exercise data for a specific person.

- `<person_name> diet.txt`: This text file stores diet data for a specific person.

## Example

Here's an example to help you understand how the Health Management System works:

1. Adding Exercise Data:
   - Choose the "Add data" option.
   - Select the "Exercise" option.
   - Choose the person for whom you want to add data (e.g., Rahul).
   - Provide the exercise details and the date/time when it was performed.
   - The system will store the exercise data in the respective file.

2. Retrieving Diet Data:
   - Choose the "Retrieve data" option.
   - Select the "Diet" option.
   - Choose the person for whom you want to retrieve data (e.g., Raj).
   - The system will display the diet data for the selected person.

3. ...

## Note

- The application utilizes a simple text file-based storage system. Exercise and diet data for each person are stored in separate text files. For more advanced features and scalability, you may consider using a database or alternative storage mechanisms.

- This Health Management System provides a basic implementation and can be further enhanced with additional features, error handling, and user input validation based on your specific requirements.

