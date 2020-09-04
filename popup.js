function summarize() {

document.getElementById('clickme').disabled = true;
document.getElementById('clickme').innerText = "Processing...";

chrome.tabs.query({active: true, lastFocusedWindow: true}, tabs => {
  api_url= tabs[0].url;

  var xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
      var status=this.responseText
      if (status=="True"){
        chrome.tabs.create({url: chrome.extension.getURL('output.html')})



      }
      else{
        document.getElementById('clickme').style.backgroundColor = "Red"
        document.getElementById('clickme').innerText = "Failed: this pdf can not be processed.";
      }
      //chrome.tabs.create({url: chrome.extension.getURL('output.html')});
    }

  };

  //http://127.0.0.1:5000/wordtrend?taburl=%22dfkjd%22
  xhttp.open("GET", "http://127.0.0.1:5000/wordtrend"+"?taburl="+api_url , true);
  xhttp.send();
  //alert(api_url)

});



}
document.getElementById('clickme').addEventListener('click', summarize);
