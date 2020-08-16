

var server_url = "localhost"

$(document).ready(function(){
    console.log("Hello World!");
    $("#my-button").click(get_content);
    $.get("http://" + server_url + ":5000/history", update_global_history)
});

var local_history = [];

function change_content(data) {
    $('#my-content').text(data);
    update_local_history();
    $.get("http://" + server_url + ":5000/history", update_global_history)
}

function update_local_history() {
    // <ul>
    // <li>..</li>
    // <li>..</li>
    // <li>..</li>
    // </ul>
    var my_list = "<ul>";
    local_history.forEach(function(elem){
       my_list += "<li>" + elem + "</li>"
    });
    my_list += "</ul>";
    $("#local-history-box").html(my_list);
}

function update_global_history(global_history) {
    // <ul>
    // <li>..</li>
    // <li>..</li>
    // <li>..</li>
    // </ul>
    var my_list = "<ul>";
    global_history.forEach(function(elem){
       my_list += "<li>" + elem + "</li>"
    });
    my_list += "</ul>";
    $("#global-history-box").html(my_list);
}

function get_content() {
    var requested_name = $("#my-name").val();
    if(requested_name == "") {
        alert("Enter something");
        return;
    }
    local_history.push(requested_name);
    $.get("http://" + server_url + ":5000/greeting/" + requested_name, change_content)
}