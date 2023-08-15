import requests

p = input("1 to create event \n2 to see events\n3 delete\n")

p = int(p)

if p ==1:
    event_data = {
        "title": input("give title"),
        "date": "2023-08-15",
        "time": "15:00:00",
        "location": "Conference Hall",
        "description": "A sample event description.",
        "available_seats": 100
    }

    response = requests.post('http://127.0.0.1:5000/api/events', json=event_data)
    try:
     if response.status_code == 200:
        print("Event created successfully")
     else:
        print("Failed to create eventResponse:", response.content)
    except requests.exceptions.RequestException as e:
        print("Error:", e)    

if p ==2:
    base_url = 'http://127.0.0.1:5000'
    response = requests.get(f'{base_url}/api/events')

    if response.status_code == 200:
        events = response.json()
        for event in events:
            print("Event ID:", event['id'])
            print("Title:", event['title'])
            print("Date:", event['date'])
            print("Time:", event['time'])
            print("Location:", event['location'])
            print("Description:", event['description'])
            print("Available Seats:", event['available_seats'])
            print("---------------")
    else:
        print("Failed to retrieve events")

if p==3:
        event_id = input("id to be deleted\n")
        event_id=int(event_id)
        base_url = 'http://127.0.0.1:5000'
        response = requests.delete(f'{base_url}/api/events/{event_id}')
        if response.status_code ==200:
            print("DELETED")
        else:
            print("failed to delete")







        
    
