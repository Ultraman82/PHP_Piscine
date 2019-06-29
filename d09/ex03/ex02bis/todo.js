/* $(document).ready(function() {
  $("button").click(function() {
    var todo = prompt("Please enter your name:", "");
    if (todo == null || todo == "") {
      alert("User cancelled the prompt.");
    } else {
      var node = $("<li></li>").text(todo);
      node.click(function(e) {
        var r = confirm("Are you sure to Delete this todo?");
        if (r == true) {
          this.parentNode.removeChild(this);
        } else {
          txt = "You pressed Cancel!";
        }
      });
      $("#ft_list").prepend(node);
    }
  });
});
 */
