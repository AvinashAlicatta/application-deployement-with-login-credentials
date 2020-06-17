function loadResult(username){
  var results;
  $.ajax
      ({
          url:"http://35.154.199.82:8081/getResultsList",
          type: 'POST',
          headers: { 
                  'Accept': 'application/json',
                  'Content-Type': 'application/json'
              },
              data:username,
          dataType: 'json',
          success: function(data){
              console.log("in truncate",data);
              results = data 
              for (let index = 0; index < results.length; index++) {
                var dataarray = results[index];
                console.log(dataarray)
                var table = document.getElementById("resultTable");
                var row = table.insertRow(1);
                var cell1 = row.insertCell(0);
                var cell2 = row.insertCell(1);
                var cell3 = row.insertCell(2);
                var cell4 = row.insertCell(3);
                cell1.innerHTML = dataarray[1];
                cell2.innerHTML = dataarray[3];
                cell3.innerHTML = dataarray[4];
                cell4.innerHTML = dataarray[2];
                
              }
          },
      error: function(err) {
          console.log(err);
      }
  });

  

}
