# Event Scheduler API
- This is a simple event scheduler application that allows users to create, update, and retrieve scheduled events. The application supports events that can occur once or repeat weekly on specific days. It persists events using a JSON file for storage and provides an API for interaction.

- **Features**
  - **Create Events**: Schedule events with a name, start date, start time, and duration. Events can repeat weekly on specific days.
  - **Retrieve Events**: Get all scheduled events or a specific event by its ID.
  - **Update Events**: Modify the details of an existing event.
  - **Conflict Prevention**: Prevent scheduling of events at the same time on the same day.

- **Requirements**
  - Python 3.x
  - Flask

- **Setup Instructions**

  - Clone the repository
    ```bash
    git clone https://github.com/AbubakrShahid/event-scheduler.git
    cd event-scheduler
    ```

  - Create a virtual environment (recommended)
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

  - Install the required dependencies
    ```bash
    pip install -r requirements.txt
    ```

  - Set up the application
    The application is ready to run once the dependencies are installed.

  - Running the Application
    To start the Flask development server, run the following command:
    ```bash
    python app.py
    ```
    By default, the server will run on `http://127.0.0.1:5000/`.

- **Testing the API**

  You can test the API using tools like [Postman](https://www.postman.com/) or `curl`.

  - Get all events
    ```bash
    GET http://127.0.0.1:5000/events
    ```

  - Get a specific event
    ```bash
    GET http://127.0.0.1:5000/events/<event_id>
    ```

  - Create a new event
    ```bash
    POST http://127.0.0.1:5000/events
    Content-Type: application/json

    {
        "name": "Sample Event",
        "start_date": "2025-04-07",
        "start_time": "10:00",
        "duration": "60",
        "repeat_days": ["Monday", "Wednesday"]
    }
    ```

  - Update an existing event
    ```bash
    PUT http://127.0.0.1:5000/events/<event_id>
    Content-Type: application/json

    {
        "name": "Updated Event",
        "start_date": "2025-04-08",
        "start_time": "11:00",
        "duration": "90",
        "repeat_days": ["Tuesday"]
    }
    ```

- **Storing Events**

  By default, events are stored in an in-memory list. The application will persist events using a `events.json` file.

