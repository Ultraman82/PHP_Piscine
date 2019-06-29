window.onload = function() {
  function setCookie(name, value, days) {
    document.cookie = name + "=" + value + "" + ";path=/";
  }

  highestCookieValue = 0;

  function addTask(text) {
    console.log("adding task to DOM: " + text);

    highestCookieValue++;
    itemId = "todo" + highestCookieValue;
    setCookie(itemId, text, 10000);

    var newItem = document.createElement("LI");
    newItem.id = itemId;
    newItem.appendChild(document.createTextNode(text));

    newItem.addEventListener("click", function(eventObject) {
      var areTheySure = confirm("Are you sure you want to delete this todo?");
      if (areTheySure) {
        setCookie(eventObject.target.id, "", -1);
        eventObject.target.remove();
      }
    });

    var list = document.getElementById("ft_list");
    list.insertBefore(newItem, list.childNodes[0]);
  }

  var newButton = document.getElementById("add_item");
  newButton.addEventListener("click", function() {
    console.log("they clicked the button");
    var newTaskText = prompt("Enter the task name", "");
    if (newTaskText) {
      addTask(newTaskText);
    } else {
      console.log("cancel :(");
    }
  });

  var cookieList = document.cookie.split(";");
  for (var i = 0; i < cookieList.length; i++) {
    var cookie = cookieList[i];
    while (cookie.charAt(0) == " ") {
      cookie = cookie.substring(1);
    }
    if (cookie.indexOf("todo") === 0) {
      var brokenCookie = cookie.split("=");
      var indexOfCookie = brokenCookie[0];
      var valueofCookie = brokenCookie[1];
      setCookie(indexOfCookie, "", -1);
      addTask(valueofCookie);
    }
  }
};
