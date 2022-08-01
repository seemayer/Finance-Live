function runbackendfunction(mod_to_run,fn_to_run,params_to_pass) {

    fetch(`/function_runner/${mod_to_run}/${fn_to_run}/${params_to_pass}`)
        .then(function (response) {
            return response.text()
        })
        .then(function (text) {
            console.log('GET response text:')
            console.log(text)
        })
}

// https://stackoverflow.com/questions/47737093/json-parse-returning-object-object-instead-of-value

function fnCaller(fn_details) {
    $.ajax({
        url:"/fn_runner",
        type:"POST",
        contentType: "application/json",
        data: JSON.stringify(fn_details),
        success: function(response) {
            var j = JSON.parse(response)
            document.getElementById("mydiv").innerText = response
        }  
    })
}


function fngetJSONdata(){
    // get JSON data from file on server and log contents to the console
    $.getJSON("static/test.json", function(data){
        console.log(data)
    })
}