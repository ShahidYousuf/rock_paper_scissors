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

/*
code for playgroud
*/
const player_icon_container = document.getElementById('player_icon_container');
const bot_icon_container = document.getElementById('bot_icon_container');

const player_result_container = document.getElementById('player_result_container');
const bot_result_container = document.getElementById('bot_result_container');

const rock_icon = "<i class='fa fa-hand-rock-o text-success fs-1 mx-2' aria-hidden='true'></i>";
const paper_icon = "<i class='fa fa-hand-paper-o text-warning fs-1 mx-2' aria-hidden='true'></i>";
const scissor_icon = "<i class='fa fa-hand-scissors-o text-primary fs-1 mx-2' aria-hidden='true'></i>";

const player_icons = document.getElementsByClassName('player_icon')

const player_move_type_input = document.getElementById('player_move_type');
const bot_move_type_input = document.getElementById('bot_move_type');

const move_form = document.getElementById('move_form');

icon_mapper = {
    rock : rock_icon,
    paper : paper_icon,
    scissor : scissor_icon
}
result_mapper = {
    win : "<span class='text-success'>Win</span>",
    loss : "<span class='text-danger'>Loss</span>",
    draw : "<span class='text-warning'>Draw</span>"
}

for(let pi of player_icons) {
    pi.addEventListener('click', function(e) {
        player_move_type_input.value = this.dataset.value;
        set_icon_container(player_icon_container, player_move_type_input.value)
        bot_move_type_input.value = botMove();
        set_icon_container(bot_icon_container, bot_move_type_input.value)
        sendGameMove()
    });
}

function botMove() {
    let moves = ['rock', 'paper', 'scissor']
    let move = moves[Math.floor(Math.random()*moves.length)];
    return move
}

function sendGameMove() {
    let data = new FormData(move_form);
    let url = move_form.action
    console.log(data)
    config = {
        method: 'POST',
        body: data
    }
    fetch(url, config)
    .then(response => response.json())
    .then(data => {
        set_result_container(player_result_container, data.player_result);
        set_result_container(bot_result_container, data.bot_result)
    })
    .catch(error => {
        console.log("Error", error)
    })
}

function set_icon_container(container, move_type) {
    container.innerHTML = "";
    let html = icon_mapper[move_type]
    container.innerHTML = html;
}

function set_result_container(container, result) {
    container.innerHTML = "";
    let html = result_mapper[result]
    container.innerHTML = html;
}
