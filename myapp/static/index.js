
function validateForm()
{
    var url=document.getElementById("url").value;
    if(url=="")
    {
        alert("Url can not be empty!!")
        return false
    }
    return true
}