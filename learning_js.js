function myfunction() {
     console.log("i")
     var link = document.getElementById('submission').value
     if (link.length == 0)
     	alert("Please enter a valid link")
     else
     {
       const url = '/check?url='+link;
       window.location = url;
     }
   
}
function Home()
{
  url = '/'
  window.location = url
}
