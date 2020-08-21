

$(document).ready(function(){
    console.log("Hello World!");
    $("#my-button").click(get_content);
    $.get("/backend/history", update_global_history)
});

var local_history = [];

function change_content(data) {
    $('#my-content').text(data);
    update_local_history();
    $.get("/backend/history", update_global_history)
}

function update_history(history_list, list_id) {
    // <ul>
    // <li>..</li>
    // <li>..</li>
    // <li>..</li>
    // </ul>
    var my_list = '<ul class="list-group list-group-flush">';
    history_list.forEach(function(elem){
       my_list += '<li class="list-group-item">' + elem + "</li>"
    });
    my_list += "</ul>";
    $("#" + list_id).html(my_list);
}

function update_local_history() {
    update_history(local_history, 'local-history-box');
}

function update_global_history(global_history) {
    update_history(global_history, 'global-history-box');
}

function get_content() {
    var requested_name = $("#my-name").val();
    if(requested_name == "") {
        alert("Enter something");
        return;
    }
    if(!local_history.includes(requested_name))
        local_history.push(requested_name);
    $.get(" /backend/greeting/" + requested_name, change_content)
}