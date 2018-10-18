window.onload = function() {
    console.log("connected")
}
function deleteUser(e) {
    if(!confirm('Are you sure?'))e.preventDefault()
    return false
}