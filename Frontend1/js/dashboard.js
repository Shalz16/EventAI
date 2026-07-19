async function loadDashboard(){

    const token = localStorage.getItem("token");

    if(!token){

        window.location="index.html";

        return;

    }

    try{

        let events = await fetch(API_URL+"/events/");
        events = await events.json();

        document.getElementById("eventsCount").innerHTML=events.length;

    }

    catch{

        document.getElementById("eventsCount").innerHTML="0";

    }

    try{

        let budget = await fetch(API_URL+"/budget/");
        budget = await budget.json();

        document.getElementById("budgetCount").innerHTML=budget.length;

    }

    catch{

        document.getElementById("budgetCount").innerHTML="0";

    }

    try{

        let volunteers = await fetch(API_URL+"/volunteers/");
        volunteers = await volunteers.json();

        document.getElementById("volunteerCount").innerHTML=volunteers.length;

    }

    catch{

        document.getElementById("volunteerCount").innerHTML="0";

    }

    try{

        let registrations = await fetch(API_URL+"/registration/");
        registrations = await registrations.json();

        document.getElementById("registrationCount").innerHTML=registrations.length;

    }

    catch{

        document.getElementById("registrationCount").innerHTML="0";

    }

}

function logout() {
    localStorage.removeItem("token");
    window.location.href = "index.html";
}
<a href="events.html">📅 Events</a>
loadDashboard();