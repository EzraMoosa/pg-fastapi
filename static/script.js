function generatePassword() {
    let length = document.getElementById("length").value;
    fetch(`/generate?length=${length}`)
        .then(response => response.json())
        .then(data => {
            document.getElementById("password").value = data.password
        })
}