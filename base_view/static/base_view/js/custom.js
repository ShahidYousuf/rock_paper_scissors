const register_submit_btn = document.getElementById('btn_register');
const register_form = document.getElementById('form_register');
const alert_register_success = document.getElementById('alert_register_success');
const error_container = document.getElementById('user_register_errors');
const btn_start_playing = document.getElementById('btn_start_playing');
const side_canvas = document.getElementById('registerName');

if (register_submit_btn) {
    register_submit_btn.addEventListener('click', function(e) {
        error_container.innerHTML = ""
        e.preventDefault();
        let data = new FormData(register_form);
        let config = {
            method : 'POST',
            body : data,
        }
        fetch('/', config)
        .then(response => response.json())
        .then(data => {
           if (!data.user_registered) {
            let register_form_error_array = data.register_form_errors.name
            for (let err of register_form_error_array) {
                error_container.innerHTML += `<small>${err.message}</small>`
            }
           }
           if (data.user_registered && data.next) {
            console.log("here", data.next)
            window.location.href = data.next;
            }
        })
        .catch((error) => {
            console.error('Error:', error);
        });
    });
}