// https://stackoverflow.com/questions/47737093/json-parse-returning-object-object-instead-of-value

function fnCaller(fn_details) {
    $.ajax({
        url:"/fn_runner",
        type:"POST",
        contentType: "application/json",
        data: JSON.stringify(fn_details),
        success: function(response) {
            document.getElementById("mylog").innerText = response.logtext
        }
    })
}

function fngetJSONdata(){
    // get JSON data from file on server and log contents to the console
    $.getJSON("static/test.json", function(data){
        console.log(data)
        console.table(data)
    })
}