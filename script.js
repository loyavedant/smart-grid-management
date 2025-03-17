document.getElementById("prediction-form").addEventListener("submit", function(event) {
    event.preventDefault();
    
    let formData = {
        hour: document.querySelector("[name='hour']").value,
        day_of_week: document.querySelector("[name='day_of_week']").value,
        temperature: document.querySelector("[name='temperature']").value,
        humidity: document.querySelector("[name='humidity']").value
    };

    fetch("/predict", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(formData)
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById("result").innerText = data.predicted_power_usage.toFixed(2);
    });
});
