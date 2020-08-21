$(document).ready(function(){
    $("#main-btn").click(calculate_answer);
});

// Updates the answer paragraph from the data from backend 
function update_answer_paragraph(data) {
    $("#answer-box").html("Your answer is " + data);
    $("#answer-box").attr("hidden", false);
}

function calculate_answer() {
    var input_number = $("#main-box").val();
    if(input_number == "") {
        alert("Enter something");
        return;
    }
    $.get("/backend/square/" + input_number, update_answer_paragraph)
}
