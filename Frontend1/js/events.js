// ================================
// EventPilot AI - Event Management
// ================================

const API_URL = "http://127.0.0.1:8000";

// Load events when page opens
window.onload = function () {
    loadEvents();
};

// ================================
// Create Event
// ================================

async function createEvent() {

    const title = document.getElementById("title").value.trim();
    const description = document.getElementById("description").value.trim();
    const venue = document.getElementById("venue").value.trim();
    const event_date = document.getElementById("event_date").value;
    const expected_participants = Number(
        document.getElementById("expected_participants").value
    );

    if (
        title === "" ||
        description === "" ||
        venue === "" ||
        event_date === "" ||
        expected_participants <= 0
    ) {
        alert("Please fill all fields.");
        return;
    }

    const response = await fetch(`${API_URL}/events/create`, {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            title,
            description,
            venue,
            event_date,
            expected_participants
        })
    });

    const data = await response.json();

    if (response.ok) {

        alert("Event Created Successfully");

        clearForm();

        loadEvents();

    } else {

        console.log(data);

        alert("Failed to create event");

    }

}

// ================================
// Load Events
// ================================

async function loadEvents() {

    const response = await fetch(`${API_URL}/events/`);

    const events = await response.json();

    const table = document.getElementById("eventTable");

    table.innerHTML = "";

    events.forEach(event => {

        table.innerHTML += `

        <tr>

            <td>${event.title}</td>

            <td>${event.description}</td>

            <td>${event.venue}</td>

            <td>${event.event_date}</td>

            <td>${event.expected_participants}</td>

            <td>

                <button onclick="deleteEvent('${event._id}')">
                    Delete
                </button>

            </td>

        </tr>

        `;

    });

}

// ================================
// Delete Event
// ================================

async function deleteEvent(id) {

    if (!confirm("Delete this event?"))
        return;

    const response = await fetch(`${API_URL}/events/${id}`, {
        method: "DELETE"
    });

    if (response.ok) {

        alert("Deleted Successfully");

        loadEvents();

    } else {

        alert("Delete Failed");

    }

}

// ================================
// Clear Form
// ================================

function clearForm() {

    document.getElementById("title").value = "";

    document.getElementById("description").value = "";

    document.getElementById("venue").value = "";

    document.getElementById("event_date").value = "";

    document.getElementById("expected_participants").value = "";

}