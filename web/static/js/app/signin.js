document.getElementById('test').addEventListener('submit', async (e) => {
    e.preventDefault();
    let data = new FormData(e.target);
    let response = await fetch("http://127.0.0.1:8000/api/v1/auth/token", {
        method: 'POST',
        body: JSON.stringify(
            {
                'username': data.get('username'),
                'password': data.get('password')
            }
        ),
        headers: {
            'Content-Type': 'application/json'
        }
    })
        .then(response => response.json())
        .then(val => {
            return val
        })
        .catch(error => {
            return JSON.parse(JSON.stringify({
                'status': false, 'message': "An error occurred"
            }))
        })
    if (response.status) {
        localStorage.setItem('token', response.token);
        Swal.fire({
            icon: 'success',
            title: 'Great',
            text: response.message,
        })
        history.back();
    } else {
        Swal.fire({
            icon: 'error',
            title: 'Oops',
            text: response.message,
        })
    }
})