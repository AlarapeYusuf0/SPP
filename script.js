function predict() {
    const attendance = document.getElementById('attendance').value;
    const first_term = document.getElementById('first_term').value;
    const second_term = document.getElementById('second_term').value;
    const ca_score = document.getElementById('ca_score').value;

    fetch('/predict', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            attendance: attendance,
            first_term: first_term,
            second_term: second_term,
            ca_score: ca_score
        })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('result').innerText =
            data.prediction;
    });
}

