$(document).ready(function(){
    $("#main-btn").click(query_song);
});

function update_results(data) {
    if(data == "NA") {
        $("#results").attr("hidden", true);
        $("#not-found").attr("hidden", false);
    } else {
        $("#not-found").attr("hidden", true);
        $("#results-iframe").attr("src", "https://youtube.com/embed/" + data);
        $("#results").attr("hidden", false);
    }
}

function query_song() {
    input_string = $("#input_string").val();
    $.get("/backend/song_search", {
        input_string: input_string
    }, update_results)
}